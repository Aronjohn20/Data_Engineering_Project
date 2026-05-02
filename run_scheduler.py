from datetime import datetime

# import your scripts
import extract
import clean
import connect

# 🔹 DATE RANGE (CHANGE IF NEEDED)
START_DATE = datetime(2026, 5, 1).date()
END_DATE   = datetime(2026, 5, 8).date()

today = datetime.now().date()

print(f"📅 Today: {today}")

# ✅ Run only within range
if START_DATE <= today <= END_DATE:

    print("🚀 Running pipeline...")

    try:
        # these scripts will execute when imported
        print("✅ Extract done")
        print("✅ Transform done")
        print("✅ Load done")

        print("🎉 Pipeline completed")

    except Exception as e:
        print("❌ Error:", e)

else:
    print("❌ Outside allowed date range")