import sys
import argparse
from mpyc.runtime import mpc

# Skapa säker heltalstyp (32-bit)
secint = mpc.SecInt()

async def main():
    # Använd argparse för att hantera kommandoradsargument
    parser = argparse.ArgumentParser(description="MPC Secure Sum Computation")
    parser.add_argument('secret_value', type=int, help="Hemmelig siffra att beräkna med")
    parser.add_argument('--hosts', required=True, help="Väg till hosts-fil med IP och port (t.ex. mpyc_hosts)")
    args = parser.parse_args()

    # Läs in IP och port från hosts-fil
    with open(args.hosts, 'r') as file:
        hosts = file.read().splitlines()

    # Dela upp IP:port och spara
    parties = [host.split(":") for host in hosts]

    # Starta MPC-runtime
    await mpc.start()

    # Konvertera till ett säkert tal och dela det
    secret_value = secint(args.secret_value)
    shared_input = mpc.input(secret_value)

    # Koppla upp till varje party (maskin)
    connections = []
    for party in parties:
        ip, port = party[0], int(party[1])
        connection = await mpc.communication.connect(ip, port)
        connections.append(connection)

    # Summera alla deltagares inputs
    total = await mpc.output(sum(shared_input))
    print(f"[Part {mpc.pid}] Summan av alla inputs är: {total}")

    # Stäng av MPC-runtime
    await mpc.shutdown()

# Starta MPC-beräkning
mpc.run(main())
