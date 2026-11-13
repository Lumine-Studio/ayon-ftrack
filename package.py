name = "ftrack"
version = "1.6.10-LMN.1"
title = "ftrack"
client_dir = "ayon_ftrack"

# Images are pulled from ynput's registry, which only publishes upstream
# tags. Keep this pinned to the upstream base version, not the LMN stamp.
service_image_tag = "1.6.10"

services = {
    "leecher": {
        "image": f"ynput/ayon-ftrack-leecher:{service_image_tag}"
    },
    "processor": {
        "image": f"ynput/ayon-ftrack-processor:{service_image_tag}"
    },
    "transmitter": {
        "image": f"ynput/ayon-ftrack-transmitter:{service_image_tag}"
    },
}

plugin_for = ["ayon_server"]

ayon_required_addons = {
    "core": ">=0.4.3",
}
ayon_compatible_addons = {
    "applications": ">=0.2.4",
}
