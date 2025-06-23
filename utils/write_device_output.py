'''Module for file writing'''

def write_device_output(device, num):
    '''Write device output into the file'''

    if device['type'] == 'ATM':
        device_type = 'ATM'
    else:
        device_type = device['type']

    return f"""
{num} ATM

Device type: {device_type}
Latitude: {device['latitude']}
Longitude: {device['longitude']}
Address: {device['fullAddressEn']}
Place: {device['placeEn']}
"""