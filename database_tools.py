import sqlite3
import os
from typing import List, Dict, Any, Optional

# Database file path
DB_PATH = "gizzele_portfolio.db"

def init_database():
    """
    Initialize Gizzele's portfolio database with her profile, hobbies, projects, and favorites.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create profile table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profile (
        profile_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        species TEXT,
        profession TEXT,
        bio TEXT
    )
    """)

    # Create hobbies table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hobbies (
        hobby_id INTEGER PRIMARY KEY,
        hobby_name TEXT NOT NULL,
        description TEXT
    )
    """)

    # Create projects table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        project_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        year INTEGER,
        role TEXT
    )
    """)

    # Create favorites table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS favorites (
        fav_id INTEGER PRIMARY KEY,
        category TEXT NOT NULL,
        item TEXT NOT NULL,
        reason TEXT
    )
    """)

    # Insert Gizzele’s data only if empty
    if cursor.execute("SELECT COUNT(*) FROM profile").fetchone()[0] == 0:
        # Profile
        cursor.execute(
            "INSERT INTO profile (name, species, profession, bio) VALUES (?, ?, ?, ?)",
            (
                "Gizzele",
                "Gazelle",
                "Singer, Performer, Advocate",
                "Gizzele is a vibrant gazelle from Zootopia, known for her music, stage charisma, and passion for promoting harmony between predator and prey."
            )
        )

        # Hobbies
        cursor.executemany(
            "INSERT INTO hobbies (hobby_name, description) VALUES (?, ?)",
            [
                ("Singing", "Performing soulful songs that inspire the city of Zootopia."),
                ("Dancing", "Energetic stage dances that mix elegance with power."),
                ("Community Work", "Engaging in charity concerts and advocating peace."),
                ("Fashion", "Designing and collaborating on colorful outfits for shows."),
                ("Fitness", "Practicing yoga and training to stay in top performance shape.")
            ]
        )

        # Projects
        cursor.executemany(
            "INSERT INTO projects (title, description, year, role) VALUES (?, ?, ?, ?)",
            [
                ("Harmony Concert", "A city-wide performance uniting predators and prey.", 2021, "Lead Singer"),
                ("Voices of Zootopia", "An album capturing the city’s diversity in music.", 2022, "Vocalist & Producer"),
                ("Charity Gala for Orphans", "Raised funds to support young animals in need.", 2023, "Performer & Host"),
                ("Gazelle Fitness Campaign", "A motivational project encouraging health and positivity.", 2023, "Ambassador"),
                ("Zootopia Peace Festival", "Annual cultural event spreading acceptance and unity.", 2024, "Organizer & Headliner")
            ]
        )

        # Favorites
        cursor.executemany(
            "INSERT INTO favorites (category, item, reason) VALUES (?, ?, ?)",
            [
                ("Food", "Fresh Green Salads", "Light, healthy, and refreshing before a show."),
                ("Drink", "Herbal Tea", "Helps soothe her voice after long rehearsals."),
                ("Music Genre", "Pop with Jazz Influence", "Energetic yet soulful."),
                ("Color", "Gold", "Represents brilliance and positivity."),
                ("Flower", "Sunflower", "Bright, tall, and always facing the light."),
                ("Animal Friend", "Cats", "Loves their elegance and independence."),
                ("Relaxation", "Spa & Yoga", "Keeps her mind and body balanced."),
                ("Dislike", "Negativity", "She avoids drama and conflict whenever possible.")
            ]
        )

    conn.commit()
    conn.close()
    return "Gizzele’s Portfolio Database initialized."

def execute_sql_query(query: str) -> List[Dict[str, Any]]:
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(query)
        if query.strip().upper().startswith("SELECT"):
            rows = cursor.fetchall()
            result = [{k: row[k] for k in row.keys()} for row in rows]
        else:
            result = [{"affected_rows": cursor.rowcount}]
            conn.commit()
        conn.close()
        return result
    except sqlite3.Error as e:
        return [{"error": str(e)}]

def get_table_schema() -> Dict[str, List[Dict[str, str]]]:
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        schema = {}
        for table in tables:
            table_name = table[0]
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = cursor.fetchall()
            schema[table_name] = [
                {"name": col[1], "type": col[2], "notnull": bool(col[3]), "pk": bool(col[5])}
                for col in columns
            ]
        conn.close()
        return schema
    except sqlite3.Error as e:
        return {"error": str(e)}

def text_to_sql(sql_query: str) -> Dict[str, Any]:
    if not os.path.exists(DB_PATH):
        init_database()
    try:
        results = execute_sql_query(sql_query)
        return {"query": sql_query, "results": results}
    except Exception as e:
        return {"query": sql_query, "results": [{"error": str(e)}]}

def get_database_info() -> Dict[str, Any]:
    if not os.path.exists(DB_PATH):
        init_database()
    schema = get_table_schema()
    sample_data = {}
    for table_name in schema.keys():
        if isinstance(table_name, str):
            try:
                sample_data[table_name] = execute_sql_query(f"SELECT * FROM {table_name} LIMIT 3")
            except:
                pass
    return {"schema": schema, "sample_data": sample_data}

if __name__ == "__main__":
    print(init_database())
    print("Gizzele’s Portfolio Database created with sample data.")
