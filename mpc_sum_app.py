import sys
import logging
from mpyc.runtime import mpc

# Configure logging to display debug messages
logging.basicConfig(level=logging.DEBUG)

# Define secure integer type (32-bit default)
secint = mpc.SecInt()

async def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <secret_value> [additional MPyC options like -M, -I, -P, --hosts]")
        sys.exit(1)

    # Parse the secret input value
    my_input = int(sys.argv[1])
    logging.debug(f"Starting MPC runtime for input value: {my_input}")

    # Start the MPyC runtime (reads MPyC CLI options automatically)
    await mpc.start()

    # Wrap the Python int as a secure integer
    secret_value = secint(my_input)
    # Distribute secret shares to all parties
    shared_inputs = mpc.input(secret_value)

    # Compute the sum securely and reveal the result
    total = await mpc.output(mpc.sum(shared_inputs))
    logging.info(f"[Party {mpc.pid}] The sum of all inputs is: {total}")

    # Shutdown the MPyC runtime
    await mpc.shutdown()

if __name__ == '__main__':
    mpc.run(main())
