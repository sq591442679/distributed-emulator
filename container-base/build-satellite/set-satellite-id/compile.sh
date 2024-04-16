currentpath=$(dirname "$(readlink -f "$0")")
cd $currentpath
gcc set_satellite_id.c -o set_satellite_id -lm $(pkg-config --cflags --libs libnl-3.0)