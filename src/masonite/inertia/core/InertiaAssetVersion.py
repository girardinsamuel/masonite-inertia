import hashlib

from masonite.helpers import config


def inertia_asset_version():
    manifest = config("inertia.public_path") + "/mix-manifest.json"

    hasher = hashlib.md5()
    with open(manifest, "rb") as manifest_file:
        buf = manifest_file.read()
        hasher.update(buf)
    return hasher.hexdigest()
