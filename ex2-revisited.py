import pyeapi
from pprint import pprint
import argparse

def check_vlan(a_list,vlan_id):
    vlan_data=a_list[0]['result']['vlans']
    vlans=vlan_data.keys()
    for vlan in vlans:
       if int(vlan_id) != int(vlan):
            continue
       elif int(vlan_id) == int(vlan):
            vlan_name=vlan_data[str(vlan)]['name']
            my_list=[vlan_id,vlan_name]
            return my_list
       else:
            return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("vlan_id", help="vlan_id ",type=int)
    parser.add_argument("--name", help="vlan_name_option",type = str)
    parser.add_argument("--remove", help="option to remove the vlan",action="store_true")
    
    args = parser.parse_args()
    vlan_id=args.vlan_id
    remove=args.remove
    vlan_name=args.name
    print vlan_name
    data={}
    pynet_sw1=pyeapi.connect_to('pynet-sw1')
    show_vlan_data=pynet_sw1.enable('show vlan')
    my_list=check_vlan(show_vlan_data,vlan_id)
    if my_list:
        result=True
        vlan_name_current=my_list[1]
    else:
        result=False    
        vlan_name_current=None  
    


    if remove:
        if result:
            print 'VLAN exists, we will remove it \n'
            command_str = 'no vlan {}'.format(vlan_id)
            pynet_sw1.config(command_str)

        else:
            print 'VLAN doesnt exist, thus there is no point to remove it'

    else:
        if result:
             if str(vlan_name) != str(vlan_name_current):
                    print type(vlan_name),type(vlan_name_current)
                    print 'VLAN exists Adding VLAN name'
                    command_str1 = 'vlan {}'.format(vlan_id)
                    cmd=[command_str1]
                    command_str2 = 'name {}'.format(vlan_name)
                    cmd.append(command_str2)
                    print cmd
                    pynet_sw1.config(cmd)
             else:
                    print ' VLAN with same ID and name exists'
        else:
             
             if vlan_name != None:
                    print 'VLAN doesnt exist pushing VLAN ID and name'
                    command_str1 = 'vlan {}'.format(vlan_id)
                    cmd=[command_str1]
                    command_str2 = 'name {}'.format(vlan_name)
                    cmd.append(command_str2)
                    pynet_sw1.config(cmd)
             else: 
                    print 'No VLAN name is passed, pushign VLAN ID'
                    command_str = 'vlan {}'.format(vlan_id)
                    pynet_sw1.config([command_str])

if __name__ == '__main__':
    main()
