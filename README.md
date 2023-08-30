# Alarm Repeater
Ignition Exchange Resource - Alarm Repeater

Ignition Exchange Resource Link: https://inductiveautomation.com/exchange/2542/overview

This is an Ignition Perspective template that displays alarms from specified tags in a table. It is designed to be used in an EmbeddedView Perspective element in any Perspective view.

## Demo
![localhost_8088_data_perspective_client_IgnitionExchange (1) (1)](https://github.com/wendajrrc/alarm-status-repeater/assets/118560778/fe587889-614e-457c-9fcf-6d21817fa2b5)

# Requirements
1. [Ignition](https://inductiveautomation.com/downloads/) with version of 8.1.10 or higher installed
   * Need to include Perspective module in installation
   * Older Ignition versions might work, they are not tested yet.

# Installtion of this template
1. Download this repository as .zip file and [import resource in Ignition Designer](https://docs.inductiveautomation.com/display/DOC81/Project+Export+and+Import#:~:text=In%20Designer%2C%20select%20File%20%3E%20Import,default%2C%20all%20resources%20are%20selected.)

# Usage
Use `AlarmRepeater/Repeater` in the EmbeddedView Perspective element in any Perspective view you wish.

## `AlarmRepeater/Repeater` major Parameters
`tagPaths`: Array/List[str]. This parameter should consist of tag paths of tags and UDT with alarms that you wish to display.

`excludePriority`: Array/List[str]. Leave it empty if you wish to include all levels of alarms. Exclude alarms with specified levels from this list. Example: ["Low", "Diagnostic"] will exclude Low and Diagnostic alarms in the alarm. Values: Diagnostic
, Low
, Medium
, High
, Critical

`recursive`: Boolean. True if you want to include alarms in subfolders in UDT tags. False to exclude alarms from the UDT subfolders.


