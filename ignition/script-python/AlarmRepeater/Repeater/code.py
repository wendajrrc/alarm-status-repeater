def getAlarmsPaths(config, currentTagPath, instances=[], templateParams={}, recursive=False, alarmReplace={},
                   excludePriority={"Diagnostic"}):
    """
    recursively search for the alarms in the alarm paths
    :param config: Dict. The configuration result from system.tag.getConfiguration function
    :param currentTagPath: String. The current base tag path.
    :param instances: List. A list consisting of all found alarm paths, for Perspective template repeater
    :param templateParams: Dict. The parameter for template.
    :param recursive: Bool. True to enable recursive search for all alarms under that path
    :param alarmReplace: Dict. Value to replace in the alarm names
    :param excludePriority: Set. Set of alarms with priority to exclude.
    :return:
    """
    if 'alarms' in config.keys():
        for alarm in config['alarms']:
            if "priority" not in alarm:
                alarm["priority"] = "Low"
            if str(alarm["priority"]) in excludePriority:
                continue
            _params = dict(templateParams)
            _name = alarm['name']
            _params["displayName"] = _name if _name not in alarmReplace.keys() else alarmReplace[_name]
            _params["tagPath"] = currentTagPath + "/Alarms/" + alarm['name'] + ".IsActive"
            instances.append(_params)

    if 'tags' in config.keys():
        for tag in config['tags']:
            getAlarmsPaths(tag, currentTagPath + "/" + str(tag['path']), instances, templateParams, recursive,
                           alarmReplace,
                           excludePriority)


def loadRepeater(tagPaths, templateParams, sortAsc=True, alarmNameReplaceOrigin=None,
                 alarmNameReplaceValue=None, excludePriority=set([]), recursive=True):
    tr_ins = []
    alarmReplace = {}
    if alarmNameReplaceOrigin is not None and alarmNameReplaceValue is not None and len(alarmNameReplaceOrigin) == len(
            alarmNameReplaceValue):
        alarmReplace = {key: value for key, value in zip(alarmNameReplaceOrigin, alarmNameReplaceValue)}

    for tagPath in tagPaths:
        config = system.tag.getConfiguration(tagPath, recursive)[0]
        getAlarmsPaths(config, str(tagPath), instances=tr_ins,
                       templateParams=templateParams, recursive=recursive, alarmReplace=alarmReplace,
                       excludePriority=excludePriority)

    tr_ins = sorted(tr_ins, key=lambda x: x['displayName'], reverse=sortAsc)

    return tr_ins