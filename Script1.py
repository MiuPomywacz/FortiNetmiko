from netmiko import ConnectHandler

# Parametry urządzenia FortiGate
fortigate = {
    'device_type': 'fortinet',
    'ip': '192.168.1.46',
    'username': 'admin',
    'password': 'admin',
}

# Inicjalizacja połączenia z urządzeniem FortiGate
try:
    net_connect = ConnectHandler(**fortigate)
    net_connect.enable()

    # Polecenie ping
    ping_command = "execute ping 8.8.8.8"
    output = net_connect.send_command(ping_command)

    # Wyświetlenie wyników
    print(output)

except Exception as e:
    print("Błąd podczas próby połączenia z urządzeniem FortiGate:", str(e))
finally:
    # Zamknięcie połączenia
    net_connect.disconnect()