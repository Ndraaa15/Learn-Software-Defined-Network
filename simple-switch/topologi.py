from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def simple_switch_topology():
  net = Mininet(controller=Controller, switch=OVSSwitch)

  info('*** Adding controller\n')
  net.addController('c0')

  info('*** Adding hosts\n')
  h1 = net.addHost('h1')
  h2 = net.addHost('h2')

  info('*** Adding switch\n')
  s1 = net.addSwitch('s1')

  info('*** Creating links\n')
  net.addLink(h1, s1)
  net.addLink(h2, s1)

  info('*** Starting network\n')
  net.start()

  info('*** Running CLI\n')
  CLI(net)

  info('*** Stopping network\n')
  net.stop()

if __name__ == '__main__':
  setLogLevel('info')
  simple_switch_topology()  