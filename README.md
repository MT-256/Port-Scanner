# Port-Scanner

IPV4 port scanner with TCP connection made in python

# Usage

This script has two parameters, first there is the -t that refers to "Target" Example -t 172.16.0.111 and another that refers to -p "Port" Example -p 0-65535(Range), -p 80(Single), -p 1,2,3,4,5(Multiple individual ports)

Range

```
python3 Port_Scanner.py -t 172.16.0.174 -p 0-65535
```

![image](https://github.com/MT-256/Port-Scanner/assets/127991386/65ff16cf-f900-49f4-9c68-3b553e89d42d)


Single

```
python3 Port_Scanner.py -t 172.16.0.174 -p 80
```

![image](https://github.com/MT-256/Port-Scanner/assets/127991386/d7e6141f-5081-4792-83fd-5e2fe7e0eac5)


Multiple individual ports

```
python3 Port_Scanner.py -t 172.16.0.174 -p 80,139,445,1000,39
```

![image](https://github.com/MT-256/Port-Scanner/assets/127991386/0830bad9-e79a-472a-8c1c-cc45edf2135b)
