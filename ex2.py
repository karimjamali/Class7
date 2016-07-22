import pyeapi
from pprint import pprint
import argparse

def check_vlan(a_list,vlan_id):
    vlan_data=a_list[0]['result']['vlans']
    vlans=vlan_data.keys()
    for vlan in vlans:
        if int(vlan_id) != int(vlan):
            continue
        else:
            return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("vlan_id", help="vlan_id ",type=int)

    parser.add_argument("--remove", help="option to remove the vlan",action="store_true")

    args = parser.parse_args()
    vlan_id=args.vlan_id
    remove=args.remove
    data={}
    pynet_sw1=pyeapi.connect_to('pynet-sw1')
    show_vlan_data=pynet_sw1.enable('show vlan')
    result=check_vlan(show_vlan_data,vlan_id)
    
    if remove:
        if result:
            print 'VLAN exists, we will remove it \n'
            command_str = 'no vlan {}'.format(vlan_id)
            pynet_sw1.config([command_str])

        else:
            print 'VLAN doesn\'t exist, thus there is no point to remove it'

    else:
        if result:
             print 'VLAN exists, we will not create it'
        else:
             print 'Adding VLAN'
             command_str = 'vlan {}'.format(vlan_id)
             pynet_sw1.config([command_str])

if __name__ == '__main__':
    main()
