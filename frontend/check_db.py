from pymongo import MongoClient

# 🔐 MongoDB connection string
MONGO_URL = "mongodb+srv://LeafDisease:yasisvQUPDZlzrdX@cluster0.sausgkt.mongodb.net/?appName=Cluster0"

# 🌿 Your class names
CLASS_NAMES = [
    "bean_angular_leaf_spot","bean_bean_rust","bean_healthy",
    "corn_blight","corn_common_rust","corn_gray_leaf_spot","corn_healthy",
    "mango_anthracnose","mango_bacterial_canker","mango_cutting_weevil",
    "mango_die_back","mango_gall_midge","mango_healthy",
    "mango_powdery_mildew","mango_sooty_mould",
    "non_leaf",
    "potato_bacteria","potato_fungi","potato_healthy","potato_nematode",
    "potato_pest","potato_phytopthora","potato_virus",
    "rice_bacterial_leaf_blight","rice_brown_spot","rice_healthy",
    "rice_leaf_blast","rice_leaf_scald","rice_narrow_brown_spot",
    "rice_neck_blast","rice_rice_hispa","rice_sheath_blight","rice_tungro",
    "tomato_bacterial_spot","tomato_early_blight","tomato_healthy",
    "tomato_late_blight","tomato_leaf_mold","tomato_powdery_mildew",
    "tomato_septoria_leaf_spot","tomato_spider_mites_two_spotted_spider_mite",
    "tomato_target_spot","tomato_tomato_mosaic_virus",
    "tomato_tomato_yellow_leaf_curl_virus"
]

try:
    # ✅ Connect to MongoDB
    client = MongoClient(MONGO_URL)
    client.admin.command('ping')
    print("✅ Connected to MongoDB\n")

    # 🔍 Step 1: Show DB names
    print("📂 Available Databases:")
    db_names = client.list_database_names()
    print(db_names)

    # 👉 CHANGE THIS AFTER SEEING OUTPUT
    db = client[db_names[0]]   # temporary auto-select

    # 🔍 Step 2: Show collections
    print("\n📁 Collections in DB:")
    collections = db.list_collection_names()
    print(collections)

    # 👉 CHANGE THIS AFTER SEEING OUTPUT
    collection = db[collections[0]]  # temporary auto-select

    # 🔍 Step 3: Print sample document
    print("\n📄 Sample Document:")
    sample = collection.find_one()
    print(sample)

    # 👉 CHANGE FIELD NAME IF NEEDED
    FIELD_NAME = "disease_name"   # update if different

    # 🔍 Step 4: Get all disease names from DB
    db_diseases = []

    for doc in collection.find():
        if FIELD_NAME in doc:
            db_diseases.append(str(doc[FIELD_NAME]).lower())

    print(f"\n📊 Total diseases in DB: {len(db_diseases)}")

    # 🔍 Step 5: Compare with CLASS_NAMES
    present = []
    missing = []

    for class_name in CLASS_NAMES:
        class_clean = class_name.lower()

        # remove crop prefix (bean_, corn_, etc.)
        parts = class_clean.split("_")
        short_name = "_".join(parts[1:]) if len(parts) > 1 else class_clean

        found = False

        for db_name in db_diseases:
            if short_name in db_name or db_name in short_name:
                found = True
                break

        if found:
            present.append(class_name)
        else:
            missing.append(class_name)

    # 📊 Results
    print("\n================ RESULT ================")

    print(f"\n✅ MATCHED ({len(present)}):")
    for d in present:
        print("✔", d)

    print(f"\n❌ MISSING ({len(missing)}):")
    for d in missing:
        print("✖", d)

    print("\n=======================================")

except Exception as e:
    print("❌ Error:", e)