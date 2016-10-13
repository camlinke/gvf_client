# gvf_receive
Receive's mobile stream from gvf_server (private repo).

## Installing
```
pip install socketIO-client
```

## Example Code
Navigate to gvf_receive folder and run example.py. Note that someone will be needing to be running the iOS app in order to see results.
```
python example.py
```

## Data Stream
Incoming data is a dictionary of results. Each result contains a UUID for that device and one of three results:

Gyro data (rotation) - updated by device every 0.5 seconds
```
{u'rotation_y': u'-0.14119', u'rotation_x': u'0.0699794', u'rotation_z': u'0.10947', u'id': u'40185FFF-F7BE-4839-B48C-F2A99D6792B2'}
```
Accelerometer data - updated by device every 0.5 seconds
```
{u'acceleration_z': u'-0.982147', u'id': u'40185FFF-F7BE-4839-B48C-F2A99D6792B2', u'acceleration_y': u'-0.215591', u'acceleration_x': u'-0.112701'}
```

Touch Data - Updated on all new touch events. Based on location from top left corner divided by screen size to normalize for different screens.
```
{u'id': u'40185FFF-F7BE-4839-B48C-F2A99D6792B2', u'touch_y': u'0.460145', u'touch_x': u'0.378422'}
```

## Compatability
Tested with Python 2.7+ and 3.4+

## Notes
It usually takes a few moments after the app loads to start transmitting data.

You can see streaming results at [138.68.16.188](http://138.68.16.188/). Note that someone will be needing to be running the iOS app in order to see results.