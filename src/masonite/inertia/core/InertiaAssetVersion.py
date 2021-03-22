import hashlib

from masonite.utils.structures import load



def inertia_asset_version(application):
    # manifest = load("inertia.public_path") + "/mix-manifest.json"
    # TODO: how to handle this in M4 ?
    # generrally speakign how to fetch package config file? what do we assume
    manifest = (
        load(application.make("config.inertia")).PUBLIC_PATH + "/mix-manifest.json"
    )
    hasher = hashlib.md5()
    with open(manifest, "rb") as manifest_file:
        buf = manifest_file.read()
        hasher.update(buf)
    return hasher.hexdigest()
