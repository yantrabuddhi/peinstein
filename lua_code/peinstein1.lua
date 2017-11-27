--prof. einstein
--lua 5.1.4, nodemcu
--please see nodemcu documentation for functions
--Author: Mandeep Singh Bhatia
--Date: 27 Oct, 2017
--

--this function needs to be called for new or change of wifi ap once
function init_wifi(ssid,pass)
	wifi.setmode(wifi.STATION)
	station_cfg={}
	station_cfg.ssid=ssid
	station_cfg.pwd=pass
    station_cfg.auto=true
    station_cfg.save=true
	wifi.sta.config(station_cfg)
    wifi.sta.autoconnect(1)
end

--this function connects einstein and keeps alive 
function connect_tcp()
    header= '00053{"cmd":"activity.recieved","data":{"output":"'
    footer= '"}}'
    conn=net.createConnection(net.TCP,0)
    conn:on("receive", function(sck, pl) print(pl) end)
    conn:on("connection",function(sck, pl)
      mytmr = tmr.create()
      --30000, 3000 = 3sec works
      mytmr:register(10000, tmr.ALARM_AUTO,keep_alive )
      mytmr:start()
      --sck:send()
      end
      )
    conn:connect(8080,"192.168.1.1")
end

--this function is for passing string commands to einstien
function send_command(comm)
    strng = header .. comm .. footer
	conn:send(strng)
end

function keep_alive()
    send_command(" ")
end

--connect_tcp if wifi connected
