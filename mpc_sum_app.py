import sys
import logging
from tkinter import getint
from mpyc.runtime import mpc

async def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <secret_value> --hosts mpyc_hosts")
        sys.exit(1)

    my_input = int(sys.argv[1])

    # Log the start of the MPC process
    logging.debug(f"Starting MPC runtime for input value: {my_input}")

    # Start the MPC runtime with a debug log
    try:
        await mpc.start()
        logging.debug("MPC runtime started successfully.")
    except Exception as e:
        logging.error(f"Error starting MPC runtime: {e}")
        sys.exit(1)

    # Secure integer and input processing
    secret_value = getint(my_input)
    
    try:
        # Use mpc.input to send input to other parties
        shared_input = await mpc.input(secret_value)
        
        # Compute the sum by iterating through the shared input
        total = await mpc.output(sum(shared_input))

        logging.debug(f"[Party {mpc.pid}] Computation result: {total}")

    except Exception as e:
        logging.error(f"Error during computation: {e}")

    # Shutdown the MPC runtime after computation
    try:
        await mpc.shutdown()
        logging.debug("MPC runtime shutdown successfully.")
    except Exception as e:
        logging.error(f"Error shutting down MPC: {e}")

# Run the main function inside MPyC runtime
if __name__ == '__main__':
    mpc.run(main())
