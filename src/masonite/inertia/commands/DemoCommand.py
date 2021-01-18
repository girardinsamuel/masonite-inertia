"""A DemoCommand Command."""
import os
import json
import shutil
from cleo import Command
from masonite.packages import append_web_routes, create_controller


demo_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "demo"
)


class DemoCommand(Command):
    """
    Create a Inertia.js demo and add it to your project.

    inertia:demo
    """

    def update_package_array(self, packages={}):
        """Updates the packages array to include Bootstrap specific packages"""
        packages["@inertiajs/inertia"] = "^0.8.2"
        packages["@inertiajs/inertia-vue3"] = "^0.3.4"
        packages["@inertiajs/progress"] = "^0.2.4"
        packages["vue"] = "^3.0.5"
        packages["@vue/compiler-sfc"] = "^3.0.5"
        packages["vue-loader"] = "^16.1.2"
        packages["laravel-mix"] = "^6.0.9"
        packages["postcss"] = "^8.2.4"
        return packages

    def _compare_version(self, version1, version2):
        versions1 = [int(v) for v in version1.split(".")]
        versions2 = [int(v) for v in version2.split(".")]
        for i in range(max(len(versions1), len(versions2))):
            v1 = versions1[i] if i < len(versions1) else 0
            v2 = versions2[i] if i < len(versions2) else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0

    def _update_packages(self, dev=True):
        """Update the "package.json" file."""
        if not os.path.exists(os.path.realpath("package.json")):
            return

        configuration_key = "devDependencies" if dev else "dependencies"
        # read all dependencies
        packages = {}
        list_deps = []
        with open(os.path.realpath("package.json"), "r+") as f:
            packages = json.load(f)
            list_deps = {
                **packages.get("devDependencies", {}),
                **packages.get("dependencies", {}),
            }
            # f.seek(0)  # Rewind to beginning of file
            # f.truncate()
            # f.write(json.dumps(packages, sort_keys=True, indent=4))
        needed = self.update_package_array()
        to_install = ""
        # to_install = {}
        for dep, version in needed.items():
            if dep not in list_deps.keys():
                to_install += f"{dep}@{version[1:]} "
            elif self._compare_version(version[1:], list_deps[dep][1:]):
                to_install += f"{dep}@{version[1:]} "

        return to_install

    def _update_webpack_configuration(self):
        """Copy webpack.mix.js file into application"""
        shutil.copyfile(os.path.join(demo_path, "webpack.mix.js"), "webpack.mix.js")

    def _add_assets(self):
        """Copies javascript and vue components."""
        directory = "resources/js/pages"
        if not os.path.exists(os.path.realpath(directory)):
            os.makedirs(os.path.realpath(directory))
        shutil.copyfile(
            os.path.join(demo_path, "static/app.js"), "resources/js/inertia_demo.js"
        )
        shutil.copyfile(
            os.path.join(demo_path, "static/pages/Index.vue"),
            "resources/js/pages/Index.vue",
        )
        shutil.copyfile(
            os.path.join(demo_path, "static/pages/Hello.vue"),
            "resources/js/pages/Hello.vue",
        )

    def _add_view(self):
        """Copy the demo inertia view with assets included"""
        shutil.copyfile(
            os.path.join(demo_path, "app.html"),
            "resources/templates/inertia_demo.html",
        )

    def handle(self):
        # add demo routes
        append_web_routes(os.path.join(demo_path, "web.py"))
        # add demo view and controller
        self._add_view()
        create_controller(os.path.join(demo_path, "InertiaDemoController.py"))
        # scaffold app (.js and vue components)
        self._add_assets()
        # update dependencies
        to_install = self._update_packages()
        self._update_webpack_configuration()
        self.info("Inertia demo has been installed successfully.")
        self.comment(f"Please run 'npm install {to_install}'")
