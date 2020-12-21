# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import octoprint.util



class EnclosurePlugin(octoprint.plugin.StartupPlugin, octoprint.plugin.TemplatePlugin, octoprint.plugin.SettingsPlugin,
                      octoprint.plugin.AssetPlugin, octoprint.plugin.BlueprintPlugin,
                      octoprint.plugin.EventHandlerPlugin):
    

    # ~~ TemplatePlugin
    def get_template_configs(self):
        return [
            dict(type="settings", template="enclosureSettings.jinja2", custom_bindings=True)
            ]

    # ~~ AssetPlugin mixin
    def get_assets(self):
        return dict(
            js=["js/enclosure.js", "js/bootstrap-colorpicker.min.js"],
            css=["css/bootstrap-colorpicker.css", "css/enclosure.css"])

    # ~~ SettingsPlugin 
    def get_settings_defaults(self):
        return dict(enclosureOutputs=[])

    # ~~ Softwareupdate hook
    def get_update_information(self):
        return dict(enclosure=dict(displayName="Enclosure Plugin", displayVersion=self._plugin_version,
            # version check: github repository
            type="github_release", user="vitormhenrique", repo="OctoPrint-Enclosure", current=self._plugin_version,
            # update method: pip
            pip="https://github.com/vitormhenrique/OctoPrint-Enclosure/archive/{target_version}.zip"))

   


__plugin_name__ = "Enclosure Plugin"
__plugin_pythoncompat__ = ">=3,<4"


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = EnclosurePlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        # "octoprint.comm.protocol.gcode.queuing"       : __plugin_implementation__.hook_gcode_queuing,
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }