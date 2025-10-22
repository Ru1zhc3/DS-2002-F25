#!/usr/bin/env python3

import sys
import update_portfolio
import generate_summary
def run_production_pipeline():
    print("Running production pipeline...", file=sys.stderr)

    print("Updating portfolio...")
    update_portfolio.main()

    print("Generating summary...")
    generate_summary.main()

    print("Production pipeline completed.", file=sys.stderr)

if __name__ == "__main__":
    run_production_pipeline()