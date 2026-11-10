import sublime
import sublime_plugin
import subprocess

from SideBarEnhancements.SideBarAPI import SideBarItem, SideBarSelection, SideBarProject

class WpmToggleCommand(sublime_plugin.WindowCommand):
    def run(self, paths = []):
        wp_root_path = sublime.active_window().folders()[0]

        items = []
        for item in SideBarSelection(paths).getSelectedItems():
            items.append(item.name())

        plugin_names = " ".join(items)
        command = 'wp plugin toggle {0} --path={1} --skip-themes'.format(plugin_names, wp_root_path)
        result = subprocess.getoutput(command)

        sublime.active_window().active_view().show_popup(result)
        print(result)

class WpmUpdatePluginCommand(sublime_plugin.WindowCommand):
    def run(self, paths = []):
        wp_root_path = sublime.active_window().folders()[0]
        print(wp_root_path)
        items = []
        for item in SideBarSelection(paths).getSelectedItems():
            items.append(item.name())

        plugin_names = " ".join(items)
        command = 'wp plugin update {0} --path={1} --skip-themes'.format(plugin_names, wp_root_path)
        result = subprocess.getoutput(command)

        sublime.active_window().active_view().show_popup(result)
        print(result)

class WpmActivateThemeCommand(sublime_plugin.WindowCommand):
    def run(self, paths = []):
        wp_root_path = sublime.active_window().folders()[0]

        items = []
        for item in SideBarSelection(paths).getSelectedItems():
            items.append(item.name())

        plugin_names = " ".join(items)
        command = 'wp theme activate {0} --path={1} --skip-themes'.format(plugin_names, wp_root_path)
        result = subprocess.getoutput(command)

        sublime.active_window().active_view().show_popup(result)
        print(result)

class WpmInstallCommand(sublime_plugin.WindowCommand):
    def run(self, paths = []):
        self.window = sublime.active_window()
        view = self.window.show_input_panel(
            "Install WP Plug-in:",
            "",
            self.on_done,
            None,
            None
        )

    def on_done(self, plugin_name):
        wp_root_path = sublime.active_window().folders()[0]

        command = 'wp plugin install {0} --path={1}'.format(plugin_name, wp_root_path)
        result = subprocess.getoutput(command)

        sublime.active_window().active_view().show_popup(result)

        print(result)

class WpmUninstallCommand(sublime_plugin.WindowCommand):
    def run(self, paths = []):
        self.window = sublime.active_window()
        view = self.window.show_input_panel(
            "Uninstall WP Plug-in:",
            "",
            self.on_done,
            None,
            None
        )

    def on_done(self, plugin_name):
        wp_root_path = sublime.active_window().folders()[0]

        command = 'wp plugin uninstall {0} --deactivate --path={1}'.format(plugin_name, wp_root_path)
        result = subprocess.getoutput(command)

        sublime.active_window().active_view().show_popup(result)

        print(result)

class WpmUpdatePluginsCommand(sublime_plugin.WindowCommand):
    def run(self, paths = []):
        wp_root_path = sublime.active_window().folders()[0]

        command = 'wp plugin update --all --path={0}'.format(wp_root_path)
        result = subprocess.getoutput(command)

        sublime.active_window().active_view().show_popup('WordPress plugins updated')

        print(result)

class WpmUpdateThemesCommand(sublime_plugin.WindowCommand):
    def run(self, paths = []):
        wp_root_path = sublime.active_window().folders()[0]

        command = 'wp theme update --all --path={0}'.format(wp_root_path)
        result = subprocess.getoutput(command)

        sublime.active_window().active_view().show_popup('WordPress themes updated')
        print(result)

class WpmUpdateCoreCommand(sublime_plugin.WindowCommand):
    def run(self, paths = []):
        wp_root_path = sublime.active_window().folders()[0]

        command = 'wp core update --path={0}'.format(wp_root_path)
        result = subprocess.getoutput(command)

        sublime.active_window().active_view().show_popup('WordPress core updated')
        print(result)

class WpmTestCommand(sublime_plugin.WindowCommand):
    def run(self, paths = []):
        command = 'sleep 10'
        result = subprocess.getoutput(command)


# class WpmTestCommand(sublime_plugin.WindowCommand):
#     def run(self, paths = []):
#         items = []
#         for item in SideBarSelection(paths).getSelectedItems():
#             items.append(item.name())
#         print(" ".join(items))
