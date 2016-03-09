import pyeapi
from pprint import pprint


def intf_data(a_list):
    interface_data=a_list[0]['result']['interfaces']
    return interface_data


def main():
 data={}
 pynet_sw1=pyeapi.connect_to('pynet-sw1')
 my_list=show_interface_output=pynet_sw1.enable('show interfaces')
 my_intfs=intf_data(my_list)
 #print my_intfs
 for interface,interface_data in my_intfs.items():
    interface_counters=interface_data.get('interfaceCounters',{})
    data[interface]=(interface_counters.get('inOctets'), interface_counters.get('outOctets'))
#mI=type(show_interface_output)
#print m
# print type(interface_counters)
# print (interface_counters)
 #print data
 print "\n {:20} {:20} {:20}".format("Interface:","InOctets:","OutOctets")
 for k,v in data.items():
    print "\n {:20} {:20} {:20}".format(k,v[0],v[1])

# print data


if __name__ == '__main__':
    main()
