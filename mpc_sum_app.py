import sys
from mpyc.runtime import mpc

secint = mpc.SecInt()

async def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <secret_value> --hosts mpyc_hosts")
        sys.exit(1)

    my_input = int(sys.argv[1])

    await mpc.start()

    secret_value = secint(my_input)
    shared_input = mpc.input(secret_value)  # NO await here
    total = await mpc.output(sum(shared_input))

    print(f"[Party {mpc.pid}] The sum of all inputs is: {total}")

    await mpc.shutdown()

mpc.run(main())
