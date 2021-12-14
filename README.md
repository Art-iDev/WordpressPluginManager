[![Donate with PayPal](https://img.shields.io/badge/paypal-Donate%20with%20paypal-blue?style=for-the-badge&logo=paypal&link=https://www.paypal.com/donate/?hosted_button_id=TZ984YJ3SJEQA)](https://www.paypal.com/donate/?hosted_button_id=TZ984YJ3SJEQA)

# WordpressPluginManager

Manage your WordPress installation directly from SublimeText SideBar and Command Palette. 

## Installation

### Dependencies

You will need the [SideBarEnhancements](titoBouzout/SideBarEnhancements) package installed in your SublimeText and [WP-CLI](https://wp-cli.org/) installed globally in your machine.

### WordpressPluginManager

Clone or download this repo into your Packages/ folder.

## Features

**Right click plugin and theme management in the sidebar:**

![Right click for plugin and theme actions](https://user-images.githubusercontent.com/700448/145997958-b69f4666-e394-4973-b377-08d625e6acc2.jpg)

### Toggle plug-in

Will either activate or deactivate the selected plug-in based on its current status.

### Update plug-in and activate theme

Their names say it all.

**Command palette for more global actions:**

![Command palette](https://user-images.githubusercontent.com/700448/145997962-bf72e5fa-2419-4559-a938-e0e4fddfbb52.jpg)

### Install WP Plug-in

Will open a panel that accepts one or more plug-in slugs, separated by space. The command performed by WP-CLI is incremented with the option `--force`, meaning you can update existing plug-ins as well.

![image](https://user-images.githubusercontent.com/700448/145999750-09d6c941-2861-48b7-bf93-a2aab65b21f7.png)

### Update Core/Plug-ins/Themes

Update all the packages from the selected option.

## Disclaimer

The commands may stall ST depending on the size of your installation.

## Roadmap

* Make code more "pythony";
* Use async calls for the commands.
