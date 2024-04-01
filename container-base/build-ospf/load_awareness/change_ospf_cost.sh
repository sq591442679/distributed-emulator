# arg1: interface name
# arg2: interface cost

echo "
config ter
interface $1
ip ospf cost $2
" | vtysh > /dev/null