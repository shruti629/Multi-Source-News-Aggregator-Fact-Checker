from src.crew_setup import collection_crew, verification_crew


def run_pipeline(topic):
    print("\nStarting News Collection Crew...\n")

    collected = collection_crew.kickoff(
        inputs={"topic": topic}
    )

    # ✅ FIX 1: extract raw output
    collected_data = collected.raw

    print("\nStarting Fact Check Crew...\n")

    fact_checked = verification_crew.kickoff(
        inputs={
            "data": collected_data   # ✅ string, not object
        }
    )

    # ✅ FIX 2: extract fact check output
    fact_checked_data = fact_checked.raw

    print("\nGenerating Final Report...\n")

    report = verification_crew.kickoff(
        inputs={
            "topic": topic,
            "data": fact_checked_data   # ✅ string again
        }
    )

    print("\nFINAL REPORT\n")
    print(report.raw)


if __name__ == "__main__":
    topic = input("Enter topic: ")
    run_pipeline(topic)
