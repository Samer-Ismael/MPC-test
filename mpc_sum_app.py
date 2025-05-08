import sys
from mpyc.runtime import mpc

secint = mpc.SecInt()

async def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <secret_value> --hosts mpyc_hosts")
        sys.exit(1)

    my_input = int(sys.argv[1])

    # Start the MPyC runtime and automatically listen on port 7070
    await mpc.start()

    # Secure integer and input processing
    secret_value = secint(my_input)
    shared_input = await mpc.input(secret_value)  # Use await for input as it is an async operation
    total = await mpc.output(sum(shared_input))

    print(f"[Party {mpc.pid}] The sum of all inputs is: {total}")

    # Shut down MPyC runtime
    await mpc.shutdown()

# Run the main function inside MPyC runtime
mpc.run(main())
