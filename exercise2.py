import pyeapi
 
def modify_output(a_list,keyword):
    return a_list[0]['result'][keyword]

def check_vlan(a,vlan):
    
    if vlan in a.keys():
      return True
    else:
      return False
def create_vlan(vlan_id,vlan_name,connection_name):
   str1='vlan {}'.format(vlan_id)
   str2='name {}'.format(vlan_name)
   #print str1
   #print str2
   cmds = [str1,str2]
   connection_name.config(cmds)
def main():

  pynet_sw1=pyeapi.connect_to('pynet-sw1')

  output=pynet_sw1.enable('show vlan')

  show_vlans=modify_output(output,'vlans')
  print show_vlans.keys()
  vlan_dict={'100':'RED','200':'BLUE','300':'GREEN','311':'YELLOW','312':'ORANGE','313':'PURPLE','500':'PINK'}
  print vlan_dict.keys()
  for vlan_id,vlan_name in vlan_dict.items():
     if (check_vlan(show_vlans,vlan_id)) is True:
       print 'VLAN {} Already Exists'.format(vlan_id)
     else:
       create_vlan(vlan_id,vlan_name,pynet_sw1) 
       print 'I created VLAN {}'.format(vlan_id) 
     
  # if not check_vlan(show_vlans,vlan_id):
  #   create_vlan(vlan_id,vlan_name,pynet_sw1)
  # else:
  #    print "VLAN Already Exists"






if __name__ == '__main__':
   main()
