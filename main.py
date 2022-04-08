class Plugin:
    # The name of the plugin. This string will be displayed in the Plugin menu
    name = "MangoHud Capture Log"
    # The name of the plugin author
    author = "Saeris"

    # If the plugin should be reloaded from a call to /plugins/reload or a file change
    hot_reload = False

    # The HTML file that will be loaded when selecting the plugin in the list
    main_view_html = "main_view.html"

    # The HTML file that will be used to display a widget in the plugin main page
    # Comment this out if you don't plan to use a tile view. This will make a button with your plugin name appear
    # tile_view_html = "tile_view.html"

    # A normal method. It can be called from JavaScript using call_plugin_function("method_1", argument1, argument2)
    async def method_1(self, *args):
        pass

    # A normal method. It can be called from JavaScript using call_plugin_function("method_2", argument1, argument2)
    async def method_2(self, *args):
        pass

    # Asyncio-compatible long-running code, executed in a task when the plugin is loaded
    async def __main


    async def get_mangolog_state(self):
        # return subprocess.Popen("systemctl is-active sshd", stdout=subprocess.PIPE, shell=True).communicate()[0] == b'active\n'
        # still looking for a method to check if mangohud logger is running is running

    async def set_mangolog_state(self, **kwargs):
        print(kwargs["state"])

        if kwargs["state"]:
            print(subprocess.Popen("mangohudctl set log_session true", stdout=subprocess.PIPE, shell=True).communicate())
        else:
            print(subprocess.Popen("mangohudctl set log_session false", stdout=subprocess.PIPE, shell=True).communicate())
        
        return await self.get_ssh_state(self)
