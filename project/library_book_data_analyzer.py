import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Global default file path
DEFAULT_FILE_PATH = "library_books.csv"


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def print_header(title):
    """Print a clean formatted section header."""
    print("\n" + "=" * 60)
    print(f" {title.center(58)} ")
    print("=" * 60)


def get_numeric_columns(df):
    """Dynamically return list of numeric columns in dataframe."""
    return df.select_dtypes(include=[np.number]).columns.tolist()


def get_categorical_columns(df):
    """Dynamically return list of categorical/string columns in dataframe."""
    return df.select_dtypes(include=["object", "string", "category"]).columns.tolist()


def generate_next_book_id(df, id_column="Book_ID"):
    """Dynamically generate next Book ID by analyzing existing ID patterns."""
    if id_column not in df.columns or df.empty:
        return "B001"
    
    existing_ids = df[id_column].dropna().astype(str).str.strip().tolist()
    max_num = 0
    prefix = "B"
    pattern = re.compile(r"^([A-Za-z]+)(\d+)$")

    for item in existing_ids:
        match = pattern.match(item)
        if match:
            p, num = match.groups()
            prefix = p
            max_num = max(max_num, int(num))

    if max_num > 0:
        return f"{prefix}{max_num + 1:03d}"
    return f"B{len(df) + 1:03d}"


def save_dataset(df, file_path):
    """Safely save dataframe to CSV."""
    try:
        df.to_csv(file_path, index=False)
        print(f"\n[SUCCESS] Dataset successfully saved to '{file_path}'!")
        return True
    except Exception as e:
        print(f"\n[ERROR] Failed to save CSV file: {e}")
        return False


# ============================================================
# DATASET LOADING
# ============================================================

def load_dataset(file_path=None):
    """
    Dynamically loads the CSV dataset.
    Allows user to provide custom file path or use default.
    Cleans column headers and strips string whitespace.
    """
    try:
        if file_path is None:
            file_path = DEFAULT_FILE_PATH

        if not os.path.exists(file_path):
            print(f"\n[ERROR] File '{file_path}' not found!")
            custom_path = input("Enter valid CSV file path (or press Enter to cancel): ").strip()
            if custom_path and os.path.exists(custom_path):
                file_path = custom_path
            else:
                print("[ERROR] Could not load dataset.")
                return None, None

        df = pd.read_csv(file_path)

        if df.empty:
            print("\n[ERROR] The CSV file is empty.")
            return None, None

        # Clean column names
        df.columns = df.columns.str.strip()

        # Dynamic type conversion for numeric fields if present
        for col in ["Rating", "Price", "Available_Copies", "Publication_Year"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

        # Strip whitespace for text columns
        for col in df.select_dtypes(include=["object"]).columns:
            df[col] = df[col].astype(str).str.strip()

        print_header("LIBRARY BOOK DATA ANALYZER")
        print(f"\n[SUCCESS] Dataset loaded successfully from: '{file_path}'")
        print(f"Total Records: {len(df)} | Columns: {len(df.columns)}")
        print(f"Detected Columns: {', '.join(df.columns)}")

        return df, file_path

    except FileNotFoundError:
        print("\n[ERROR] File not found.")
    except pd.errors.EmptyDataError:
        print("\n[ERROR] CSV file is empty.")
    except pd.errors.ParserError:
        print("\n[ERROR] CSV file format is invalid.")
    except UnicodeDecodeError:
        print("\n[ERROR] Unable to read CSV encoding.")
    except Exception as e:
        print(f"\n[ERROR] while loading dataset: {e}")

    return None, None


# ============================================================
# DISPLAY BOOKS (DYNAMIC VIEWING)
# ============================================================

def display_all_books(df):
    """
    Dynamic display options:
    1. Display all books
    2. Display top N books (head)
    3. Display bottom N books (tail)
    4. Display random sample
    5. Paginated interactive view
    """
    try:
        if df is None or df.empty:
            print("\n[INFO] No books available in dataset.")
            return

        print_header("DISPLAY BOOKS MENU")
        print("1. View All Books")
        print("2. View Top N Books (Head)")
        print("3. View Bottom N Books (Tail)")
        print("4. View Random Sample of N Books")
        print("5. Paginated View (Interactive 15 books per page)")

        choice = input("\nEnter your choice (1-5, default 1): ").strip()

        if choice == "2":
            n = input("How many books to view from top? (default 10): ").strip()
            n = int(n) if n.isdigit() and int(n) > 0 else 10
            print(f"\n--- Top {n} Books ---")
            print(df.head(n).to_string(index=False))
            print(f"\nShowing {min(n, len(df))} of {len(df)} books.")

        elif choice == "3":
            n = input("How many books to view from bottom? (default 10): ").strip()
            n = int(n) if n.isdigit() and int(n) > 0 else 10
            print(f"\n--- Bottom {n} Books ---")
            print(df.tail(n).to_string(index=False))
            print(f"\nShowing {min(n, len(df))} of {len(df)} books.")

        elif choice == "4":
            n = input("How many random books to sample? (default 5): ").strip()
            n = int(n) if n.isdigit() and int(n) > 0 else 5
            sample_size = min(n, len(df))
            print(f"\n--- Random Sample of {sample_size} Books ---")
            print(df.sample(sample_size).to_string(index=False))

        elif choice == "5":
            page_size = 15
            total_pages = (len(df) + page_size - 1) // page_size
            page = 0
            while True:
                start = page * page_size
                end = min(start + page_size, len(df))
                print(f"\n--- Page {page + 1} of {total_pages} (Books {start + 1} to {end}) ---")
                print(df.iloc[start:end].to_string(index=False))
                print("\n[N] Next Page | [P] Previous Page | [Q] Exit to Menu")
                nav = input("Enter choice: ").strip().lower()
                if nav == "n" and page < total_pages - 1:
                    page += 1
                elif nav == "p" and page > 0:
                    page -= 1
                elif nav in ["q", "exit"]:
                    break
                else:
                    print("No more pages in that direction or invalid input.")

        else:
            # Default: view all
            print("\n================ ALL BOOKS ================\n")
            print(df.to_string(index=False))
            print(f"\nTotal Books: {len(df)}")

    except Exception as e:
        print(f"\n[ERROR] Displaying books: {e}")


# ============================================================
# SEARCH FUNCTIONS (SPECIFIC & DYNAMIC UNIVERSAL)
# ============================================================

def search_by_id(df):
    """Dynamic Search by Book ID with exact and partial match fallback."""
    try:
        book_id = input("\nEnter Book ID to search: ").strip()
        if not book_id:
            print("\nBook ID cannot be empty.")
            return

        # Exact match
        result = df[df["Book_ID"].astype(str).str.strip().str.lower() == book_id.lower()]

        # Fallback to partial match if exact match not found
        if result.empty:
            result = df[df["Book_ID"].astype(str).str.lower().str.contains(book_id.lower(), na=False, regex=False)]
            if not result.empty:
                print(f"\n[NOTE] Exact ID '{book_id}' not found, but found {len(result)} partial match(es):")

        if result.empty:
            print(f"\nNo book found with Book ID: '{book_id}'")
        else:
            print("\n================ BOOK DETAILS ================\n")
            print(result.to_string(index=False))
            print(f"\nTotal Matches: {len(result)}")

    except Exception as e:
        print(f"\nError searching by ID: {e}")


def search_by_name(df):
    """Dynamic partial search by Book Name."""
    try:
        book_name = input("\nEnter book name or part of name: ").strip()
        if not book_name:
            print("\nBook name cannot be empty.")
            return

        result = df[df["Book_Name"].astype(str).str.lower().str.contains(book_name.lower(), na=False, regex=False)]

        if result.empty:
            print(f"\nNo book found containing: '{book_name}'")
        else:
            print("\n================ SEARCH RESULTS ================\n")
            print(result.to_string(index=False))
            print(f"\nBooks Found: {len(result)}")

    except Exception as e:
        print(f"\nError searching by name: {e}")


def books_by_author(df):
    """Dynamic partial search by Author."""
    try:
        author = input("\nEnter Author Name: ").strip()
        if not author:
            print("\nAuthor name cannot be empty.")
            return

        result = df[df["Author"].astype(str).str.lower().str.contains(author.lower(), na=False, regex=False)]

        if result.empty:
            print(f"\nNo books found for author: '{author}'")
            # Suggest existing authors
            if "Author" in df.columns:
                print("\nAvailable Authors sample:")
                print(", ".join(df["Author"].dropna().unique()[:8]))
        else:
            print("\n================ AUTHOR BOOKS ================\n")
            print(result.to_string(index=False))
            print(f"\nTotal Books: {len(result)}")

    except Exception as e:
        print(f"\nError searching by author: {e}")


def books_by_genre(df):
    """Dynamic partial search by Genre."""
    try:
        genre = input("\nEnter Genre: ").strip()
        if not genre:
            print("\nGenre cannot be empty.")
            return

        result = df[df["Genre"].astype(str).str.lower().str.contains(genre.lower(), na=False, regex=False)]

        if result.empty:
            print(f"\nNo books found in genre: '{genre}'")
            if "Genre" in df.columns:
                print("\nAvailable Genres in library:")
                print(", ".join(sorted(df["Genre"].dropna().unique())))
        else:
            print("\n================ GENRE BOOKS ================\n")
            print(result.to_string(index=False))
            print(f"\nTotal Books: {len(result)}")

    except Exception as e:
        print(f"\nError searching by genre: {e}")


def books_by_language(df):
    """Dynamic partial search by Language."""
    try:
        language = input("\nEnter Language: ").strip()
        if not language:
            print("\nLanguage cannot be empty.")
            return

        result = df[df["Language"].astype(str).str.lower().str.contains(language.lower(), na=False, regex=False)]

        if result.empty:
            print(f"\nNo books found for language: '{language}'")
            if "Language" in df.columns:
                print("\nAvailable Languages in library:")
                print(", ".join(sorted(df["Language"].dropna().unique())))
        else:
            print("\n================ LANGUAGE BOOKS ================\n")
            print(result.to_string(index=False))
            print(f"\nTotal Books: {len(result)}")

    except Exception as e:
        print(f"\nError searching by language: {e}")


def universal_search(df):
    """
    DYNAMIC UNIVERSAL SEARCH:
    Searches across ALL columns simultaneously for any keyword or number.
    """
    try:
        query = input("\nEnter search keyword (searches across ALL columns): ").strip()
        if not query:
            print("\nSearch keyword cannot be empty.")
            return

        query_lower = query.lower()
        mask = pd.Series(False, index=df.index)

        # Check across every column
        matched_columns = {}
        for col in df.columns:
            col_match = df[col].astype(str).str.lower().str.contains(query_lower, na=False, regex=False)
            count = col_match.sum()
            if count > 0:
                matched_columns[col] = count
            mask |= col_match

        result = df[mask]

        if result.empty:
            print(f"\nNo matching records found across any column for: '{query}'")
        else:
            print("\n================ UNIVERSAL SEARCH RESULTS ================\n")
            print(result.to_string(index=False))
            print(f"\nTotal Matches Found: {len(result)}")
            print("Matched in Columns: " + ", ".join([f"{col} ({count})" for col, count in matched_columns.items()]))

    except Exception as e:
        print(f"\nError in universal search: {e}")


def dynamic_column_search(df):
    """
    DYNAMIC COLUMN SEARCH:
    Lists all columns dynamically, allows user to pick ANY column and search within it.
    """
    try:
        print_header("DYNAMIC COLUMN SEARCH")
        columns = list(df.columns)
        for idx, col in enumerate(columns, 1):
            print(f"{idx}. {col}")

        choice = input("\nSelect column number to search: ").strip()
        if not choice.isdigit() or not (1 <= int(choice) <= len(columns)):
            print("Invalid column selection.")
            return

        selected_col = columns[int(choice) - 1]
        term = input(f"Enter search query for column '{selected_col}': ").strip()
        if not term:
            print("Search query cannot be empty.")
            return

        result = df[df[selected_col].astype(str).str.lower().str.contains(term.lower(), na=False, regex=False)]

        if result.empty:
            print(f"\nNo records found in '{selected_col}' matching '{term}'.")
        else:
            print(f"\n================ RESULTS FOR '{selected_col}' ================\n")
            print(result.to_string(index=False))
            print(f"\nTotal Records Found: {len(result)}")

    except Exception as e:
        print(f"\nError in dynamic column search: {e}")


# ============================================================
# FILTERING (DYNAMIC MULTI-CRITERIA FILTER)
# ============================================================

def filter_by_rating(df):
    """Original rating filter (maintained for backward compatibility)."""
    try:
        rating_input = input("\nEnter minimum rating (0 to 5): ").strip()
        rating = float(rating_input)

        if rating < 0 or rating > 5:
            print("\nRating must be between 0 and 5.")
            return

        result = df[df["Rating"] >= rating].sort_values(by="Rating", ascending=False)

        if result.empty:
            print("\nNo books found with rating >=", rating)
        else:
            print(f"\nBooks with rating >= {rating}")
            print(result.to_string(index=False))
            print(f"\nTotal Books: {len(result)}")

    except ValueError:
        print("\nPlease enter a valid number for rating.")
    except Exception as e:
        print(f"\nError filtering by rating: {e}")


def dynamic_filter(df):
    """
    DYNAMIC MULTI-CRITERIA FILTER:
    Allows user to filter by ANY column (numeric or categorical)
    with customizable operators (>, <, >=, <=, ==, between, contains).
    Supports chained multi-step filtering.
    """
    try:
        filtered_df = df.copy()

        while True:
            print_header("DYNAMIC FILTER ENGINE")
            columns = list(filtered_df.columns)
            for idx, col in enumerate(columns, 1):
                col_type = "Numeric" if pd.api.types.is_numeric_dtype(filtered_df[col]) else "Text"
                print(f"{idx}. {col} ({col_type})")

            col_choice = input("\nSelect column number to filter (or 'q' to cancel): ").strip()
            if col_choice.lower() in ["q", "exit", ""]:
                break

            if not col_choice.isdigit() or not (1 <= int(col_choice) <= len(columns)):
                print("Invalid column choice.")
                continue

            selected_col = columns[int(col_choice) - 1]
            is_numeric = pd.api.types.is_numeric_dtype(filtered_df[selected_col])

            if is_numeric:
                print(f"\n--- Numeric Filter for '{selected_col}' ---")
                col_min = filtered_df[selected_col].min()
                col_max = filtered_df[selected_col].max()
                print(f"Current Value Range: Min = {col_min}, Max = {col_max}")
                print("1. Greater than (>)")
                print("2. Greater than or equal to (>=)")
                print("3. Less than (<)")
                print("4. Less than or equal to (<=)")
                print("5. Equal to (==)")
                print("6. Between Range (Min to Max)")

                op = input("Choose operator (1-6): ").strip()

                if op == "6":
                    low = float(input(f"Enter Minimum {selected_col}: "))
                    high = float(input(f"Enter Maximum {selected_col}: "))
                    filtered_df = filtered_df[(filtered_df[selected_col] >= low) & (filtered_df[selected_col] <= high)]
                elif op in ["1", "2", "3", "4", "5"]:
                    val = float(input(f"Enter value for {selected_col}: "))
                    if op == "1":
                        filtered_df = filtered_df[filtered_df[selected_col] > val]
                    elif op == "2":
                        filtered_df = filtered_df[filtered_df[selected_col] >= val]
                    elif op == "3":
                        filtered_df = filtered_df[filtered_df[selected_col] < val]
                    elif op == "4":
                        filtered_df = filtered_df[filtered_df[selected_col] <= val]
                    elif op == "5":
                        filtered_df = filtered_df[filtered_df[selected_col] == val]
                else:
                    print("Invalid operator selection.")
                    continue

            else:
                print(f"\n--- Text Filter for '{selected_col}' ---")
                print("1. Contains (substring)")
                print("2. Exact match")
                print("3. Starts with")

                op = input("Choose operator (1-3): ").strip()
                val = input(f"Enter search text for '{selected_col}': ").strip()

                if not val:
                    print("Text cannot be empty.")
                    continue

                if op == "1":
                    filtered_df = filtered_df[filtered_df[selected_col].astype(str).str.lower().str.contains(val.lower(), na=False, regex=False)]
                elif op == "2":
                    filtered_df = filtered_df[filtered_df[selected_col].astype(str).str.strip().str.lower() == val.lower()]
                elif op == "3":
                    filtered_df = filtered_df[filtered_df[selected_col].astype(str).str.lower().str.startswith(val.lower(), na=False)]
                else:
                    print("Invalid operator selection.")
                    continue

            print(f"\n[RESULTS] Matching records: {len(filtered_df)}")
            if filtered_df.empty:
                print("No records matched the filter criteria.")
                break
            else:
                print(filtered_df.to_string(index=False))

            # Ask to chain additional filter
            again = input("\nDo you want to apply an additional filter on this result? (y/n): ").strip().lower()
            if again not in ["y", "yes"]:
                # Option to export
                export_choice = input("Export these filtered results to a new CSV? (y/n): ").strip().lower()
                if export_choice in ["y", "yes"]:
                    export_data(filtered_df)
                break

    except Exception as e:
        print(f"\nError in dynamic filter: {e}")


# ============================================================
# DYNAMIC SORTING
# ============================================================

def sort_books(df):
    """
    DYNAMIC SORT:
    Dynamically lists all columns from the dataset.
    Allows user to select ANY column to sort by.
    Provides choice of Ascending or Descending order.
    """
    try:
        print_header("SORT BOOKS (DYNAMIC)")
        columns = list(df.columns)
        for idx, col in enumerate(columns, 1):
            print(f"{idx}. {col}")

        choice = input("\nSelect column number to sort by: ").strip()
        if not choice.isdigit() or not (1 <= int(choice) <= len(columns)):
            print("\nInvalid choice.")
            return

        column = columns[int(choice) - 1]

        print("\nSort Direction:")
        print("1. Ascending  (A to Z / Smallest to Largest)")
        print("2. Descending (Z to A / Largest to Smallest)")
        order_choice = input("Enter choice (1 or 2, default 1): ").strip()
        is_ascending = order_choice != "2"

        result = df.sort_values(by=column, ascending=is_ascending)

        direction_label = "Ascending" if is_ascending else "Descending"
        print(f"\nBooks sorted by '{column}' ({direction_label}):\n")
        print(result.to_string(index=False))

        export_choice = input("\nExport sorted result to a new CSV? (y/n): ").strip().lower()
        if export_choice in ["y", "yes"]:
            export_data(result)

    except Exception as e:
        print(f"\nError sorting books: {e}")


# ============================================================
# DYNAMIC NUMPY ANALYSIS
# ============================================================

def numpy_analysis(df):
    """
    DYNAMIC NUMPY ANALYSIS:
    Dynamically discovers all numeric columns in dataset.
    Allows analyzing ALL numeric columns or a chosen column.
    Uses NumPy for: Mean, Median, Std Dev, Variance, Min, Max, Range,
    25th/75th Percentiles, and Interquartile Range (IQR).
    """
    try:
        numeric_cols = get_numeric_columns(df)
        if not numeric_cols:
            print("\n[INFO] No numeric columns found in dataset.")
            return

        print_header("NUMPY ANALYSIS (DYNAMIC)")
        print("1. Comprehensive Analysis of ALL Numeric Columns")
        print("2. In-Depth Analysis of a Specific Column")

        choice = input("\nEnter choice (1 or 2, default 1): ").strip()

        if choice == "2":
            for idx, col in enumerate(numeric_cols, 1):
                print(f"{idx}. {col}")
            col_choice = input("Select column number: ").strip()
            if not col_choice.isdigit() or not (1 <= int(col_choice) <= len(numeric_cols)):
                print("Invalid column selection.")
                return
            selected_cols = [numeric_cols[int(col_choice) - 1]]
        else:
            selected_cols = numeric_cols

        for col in selected_cols:
            arr = df[col].dropna().to_numpy()
            if len(arr) == 0:
                print(f"\nColumn '{col}' has no valid numerical data.")
                continue

            # NumPy calculations
            count = len(arr)
            total_sum = np.sum(arr)
            mean_val = np.mean(arr)
            median_val = np.median(arr)
            std_val = np.std(arr)
            var_val = np.var(arr)
            min_val = np.min(arr)
            max_val = np.max(arr)
            range_val = np.ptp(arr)
            q25 = np.percentile(arr, 25)
            q75 = np.percentile(arr, 75)
            iqr = q75 - q25

            print(f"\n>>> NUMPY STATISTICAL PROFILE: {col} <<<")
            print(f"  Count (Sample Size)   : {count}")
            print(f"  Sum (Total)           : {round(total_sum, 2)}")
            print(f"  Mean (Average)        : {round(mean_val, 2)}")
            print(f"  Median (50th %ile)    : {round(median_val, 2)}")
            print(f"  Standard Deviation    : {round(std_val, 2)}")
            print(f"  Variance              : {round(var_val, 2)}")
            print(f"  Minimum Value         : {min_val}")
            print(f"  Maximum Value         : {max_val}")
            print(f"  Range (Max - Min)     : {round(range_val, 2)}")
            print(f"  25th Percentile (Q1)  : {round(q25, 2)}")
            print(f"  75th Percentile (Q3)  : {round(q75, 2)}")
            print(f"  IQR (Q3 - Q1)         : {round(iqr, 2)}")

    except Exception as e:
        print(f"\nError in NumPy analysis: {e}")


# ============================================================
# LIBRARY STATISTICS
# ============================================================

def library_statistics(df):
    """Dynamic dataset summary and frequency distributions."""
    try:
        print_header("LIBRARY STATISTICS")

        print(f"Total Books (Rows)        : {len(df)}")
        print(f"Total Features (Columns)  : {len(df.columns)}")

        if "Author" in df.columns:
            print(f"Total Unique Authors      : {df['Author'].nunique()}")
        if "Genre" in df.columns:
            print(f"Total Unique Genres       : {df['Genre'].nunique()}")
        if "Language" in df.columns:
            print(f"Total Unique Languages    : {df['Language'].nunique()}")
        if "Rating" in df.columns:
            print(f"Average Book Rating       : {round(df['Rating'].mean(), 2)} / 5.0")
        if "Available_Copies" in df.columns:
            print(f"Total Available Copies    : {int(df['Available_Copies'].sum())}")
        if "Price" in df.columns:
            print(f"Average Book Price        : ₹{round(df['Price'].mean(), 2)}")
            print(f"Price Range (Min - Max)   : ₹{df['Price'].min()} - ₹{df['Price'].max()}")

        # Categorical distributions
        if "Genre" in df.columns:
            print("\n--- Books by Genre ---")
            print(df["Genre"].value_counts().to_string())

        if "Language" in df.columns:
            print("\n--- Books by Language ---")
            print(df["Language"].value_counts().to_string())

        if "Author" in df.columns:
            print("\n--- Top 5 Most Frequent Authors ---")
            print(df["Author"].value_counts().head(5).to_string())

    except Exception as e:
        print(f"\nError calculating statistics: {e}")


# ============================================================
# DYNAMIC VISUALIZATIONS
# ============================================================

def generate_visualizations(df):
    """
    DYNAMIC VISUALIZATIONS:
    1. Standard Overview Dashboard (Enhanced versions of original 5 charts)
    2. Dynamic Custom Chart Builder (User picks chart type, X/Y axes, and save option)
    """
    try:
        print_header("DATA VISUALIZATION STUDIO")
        print("1. Standard Overview Dashboard (Generate all 5 standard charts)")
        print("2. Custom Dynamic Chart Builder (Interactive plot designer)")

        sub_choice = input("\nEnter choice (1 or 2, default 1): ").strip()

        if sub_choice == "2":
            # Interactive Chart Builder
            print("\n--- Select Chart Type ---")
            print("1. Bar Chart (Category Frequency or Aggregated Numeric)")
            print("2. Line Chart (Trend over sorted values)")
            print("3. Histogram / KDE (Distribution of Numeric Column)")
            print("4. Scatter Plot (Relationship between 2 Numeric Columns)")
            print("5. Box Plot (Distribution & Outliers by Category)")
            print("6. Pie Chart (Category Proportions)")
            print("7. Correlation Heatmap (All Numeric Columns)")

            chart_type = input("\nEnter chart type (1-7): ").strip()
            columns = list(df.columns)
            numeric_cols = get_numeric_columns(df)
            cat_cols = get_categorical_columns(df)

            plt.figure(figsize=(10, 6))

            if chart_type == "1":
                # Bar Chart
                print("\nAvailable Categorical Columns:", ", ".join(cat_cols))
                col = input("Select categorical column for Bar Chart: ").strip()
                if col in df.columns:
                    counts = df[col].value_counts().head(12)
                    sns.barplot(x=counts.index, y=counts.values, palette="viridis")
                    plt.title(f"Distribution of {col}", fontsize=14)
                    plt.xlabel(col, fontsize=12)
                    plt.ylabel("Count", fontsize=12)
                    plt.xticks(rotation=45)
                else:
                    print("Invalid column.")
                    return

            elif chart_type == "2":
                # Line Chart
                print("\nAvailable Numeric Columns:", ", ".join(numeric_cols))
                x_col = input("Select X-axis column: ").strip()
                if x_col in df.columns:
                    trend = df[x_col].value_counts().sort_index()
                    plt.plot(trend.index, trend.values, marker="o", color="#2b5c8f", linewidth=2)
                    plt.title(f"Trend Analysis by {x_col}", fontsize=14)
                    plt.xlabel(x_col, fontsize=12)
                    plt.ylabel("Count", fontsize=12)
                    plt.grid(True, linestyle="--", alpha=0.6)
                else:
                    print("Invalid column.")
                    return

            elif chart_type == "3":
                # Histogram / KDE
                print("\nAvailable Numeric Columns:", ", ".join(numeric_cols))
                col = input("Select numeric column for Histogram: ").strip()
                if col in df.columns:
                    bins = input("Number of bins (default 12): ").strip()
                    bins = int(bins) if bins.isdigit() else 12
                    sns.histplot(df[col].dropna(), bins=bins, kde=True, color="#4c72b0")
                    plt.title(f"Distribution of {col}", fontsize=14)
                    plt.xlabel(col, fontsize=12)
                    plt.ylabel("Frequency", fontsize=12)
                else:
                    print("Invalid column.")
                    return

            elif chart_type == "4":
                # Scatter Plot
                if len(numeric_cols) < 2:
                    print("Need at least 2 numeric columns for scatter plot.")
                    return
                print("\nAvailable Numeric Columns:", ", ".join(numeric_cols))
                x_col = input("Select X-axis numeric column: ").strip()
                y_col = input("Select Y-axis numeric column: ").strip()
                if x_col in df.columns and y_col in df.columns:
                    sns.scatterplot(data=df, x=x_col, y=y_col, hue="Genre" if "Genre" in df.columns else None, alpha=0.8, s=60)
                    plt.title(f"Scatter Plot: {x_col} vs {y_col}", fontsize=14)
                    plt.xlabel(x_col, fontsize=12)
                    plt.ylabel(y_col, fontsize=12)
                else:
                    print("Invalid column names.")
                    return

            elif chart_type == "5":
                # Box Plot
                print("\nCategorical Columns:", ", ".join(cat_cols))
                print("Numeric Columns:", ", ".join(numeric_cols))
                cat = input("Select Categorical column (e.g. Genre): ").strip()
                num = input("Select Numeric column (e.g. Price or Rating): ").strip()
                if cat in df.columns and num in df.columns:
                    sns.boxplot(data=df, x=cat, y=num, palette="Set2")
                    plt.title(f"Box Plot: {num} by {cat}", fontsize=14)
                    plt.xticks(rotation=45)
                else:
                    print("Invalid columns.")
                    return

            elif chart_type == "6":
                # Pie Chart
                print("\nAvailable Categorical Columns:", ", ".join(cat_cols))
                col = input("Select categorical column for Pie Chart: ").strip()
                if col in df.columns:
                    top_vals = df[col].value_counts().head(7)
                    plt.pie(top_vals.values, labels=top_vals.index, autopct="%1.1f%%", startangle=140, colors=sns.color_palette("pastel"))
                    plt.title(f"Top Categories in {col}", fontsize=14)
                else:
                    print("Invalid column.")
                    return

            elif chart_type == "7":
                # Heatmap
                if len(numeric_cols) >= 2:
                    corr = df[numeric_cols].corr()
                    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
                    plt.title("Correlation Matrix Heatmap", fontsize=14)
                else:
                    print("Not enough numeric columns for correlation heatmap.")
                    return

            else:
                print("Invalid chart type choice.")
                return

            plt.tight_layout()

            # Save chart option
            save_opt = input("\nSave this chart as an image? (y/n): ").strip().lower()
            if save_opt in ["y", "yes"]:
                img_name = input("Enter image filename (default 'custom_chart.png'): ").strip()
                if not img_name:
                    img_name = "custom_chart.png"
                if not img_name.endswith(".png"):
                    img_name += ".png"
                plt.savefig(img_name, dpi=300)
                print(f"[SUCCESS] Chart saved as '{img_name}'.")

            plt.show()

        else:
            # Generate Standard Overview Dashboard
            print("\nGenerating Standard Overview Charts...")

            # 1. Genre Count
            if "Genre" in df.columns:
                plt.figure(figsize=(10, 5))
                genre_count = df["Genre"].value_counts()
                sns.barplot(x=genre_count.index, y=genre_count.values, palette="mako")
                plt.title("Number of Books by Genre", fontsize=14)
                plt.xlabel("Genre", fontsize=12)
                plt.ylabel("Number of Books", fontsize=12)
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

            # 2. Publication Year Trend
            if "Publication_Year" in df.columns:
                plt.figure(figsize=(10, 5))
                year_count = df["Publication_Year"].value_counts().sort_index()
                plt.plot(year_count.index, year_count.values, marker="o", color="#d95f02", linewidth=2)
                plt.title("Books by Publication Year", fontsize=14)
                plt.xlabel("Publication Year", fontsize=12)
                plt.ylabel("Number of Books", fontsize=12)
                plt.grid(True, linestyle="--", alpha=0.6)
                plt.tight_layout()
                plt.show()

            # 3. Rating Distribution
            if "Rating" in df.columns:
                plt.figure(figsize=(8, 5))
                sns.histplot(df["Rating"].dropna(), bins=10, kde=True, color="#1b9e77")
                plt.title("Rating Distribution", fontsize=14)
                plt.xlabel("Rating", fontsize=12)
                plt.ylabel("Number of Books", fontsize=12)
                plt.tight_layout()
                plt.show()

            # 4. Top 10 Authors
            if "Author" in df.columns:
                plt.figure(figsize=(10, 5))
                top_authors = df["Author"].value_counts().head(10)
                sns.barplot(x=top_authors.index, y=top_authors.values, palette="rocket")
                plt.title("Top 10 Authors by Book Count", fontsize=14)
                plt.xlabel("Author", fontsize=12)
                plt.ylabel("Number of Books", fontsize=12)
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

            # 5. Average Rating by Genre
            if "Genre" in df.columns and "Rating" in df.columns:
                plt.figure(figsize=(10, 5))
                avg_rating = df.groupby("Genre")["Rating"].mean().sort_values(ascending=False)
                sns.barplot(x=avg_rating.index, y=avg_rating.values, palette="crest")
                plt.title("Average Rating by Genre", fontsize=14)
                plt.xlabel("Genre", fontsize=12)
                plt.ylabel("Average Rating", fontsize=12)
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

            print("\n[SUCCESS] All standard visualizations generated successfully.")

    except Exception as e:
        print(f"\nError generating visualizations: {e}")


# ============================================================
# BOOK CRUD OPERATIONS (DYNAMIC ADD, UPDATE, DELETE)
# ============================================================

def add_book(df, file_path=DEFAULT_FILE_PATH):
    """
    DYNAMIC ADD BOOK:
    - Auto-generates next sequential Book ID based on dataset pattern.
    - Interactive input with robust validation loops.
    - Appends row to dataframe and saves to CSV.
    """
    try:
        print_header("ADD NEW BOOK (DYNAMIC)")

        # Auto ID generation
        suggested_id = generate_next_book_id(df)
        id_prompt = f"Enter Book ID [Press Enter to accept '{suggested_id}']: "
        entered_id = input(id_prompt).strip()
        book_id = entered_id if entered_id else suggested_id

        # Check duplicate
        if "Book_ID" in df.columns and book_id.lower() in df["Book_ID"].astype(str).str.lower().values:
            print(f"\n[ERROR] Book ID '{book_id}' already exists in the dataset!")
            return df

        # Book Name
        while True:
            book_name = input("Enter Book Name: ").strip()
            if book_name:
                break
            print("Book name cannot be empty. Please try again.")

        # Author Name
        while True:
            author = input("Enter Author Name: ").strip()
            if author:
                break
            print("Author name cannot be empty. Please try again.")

        # Genre
        while True:
            genre = input("Enter Genre: ").strip()
            if genre:
                break
            print("Genre cannot be empty. Please try again.")

        # Publication Year
        while True:
            year_input = input("Enter Publication Year (1000 - 2100): ").strip()
            try:
                pub_year = int(year_input)
                if 1000 <= pub_year <= 2100:
                    break
                print("Please enter a year between 1000 and 2100.")
            except ValueError:
                print("Invalid input! Publication year must be an integer.")

        # Rating
        while True:
            rating_input = input("Enter Rating (0.0 to 5.0): ").strip()
            try:
                rating = float(rating_input)
                if 0.0 <= rating <= 5.0:
                    break
                print("Rating must be between 0.0 and 5.0.")
            except ValueError:
                print("Invalid input! Rating must be a number.")

        # Available Copies
        while True:
            copies_input = input("Enter Available Copies (>= 0): ").strip()
            try:
                copies = int(copies_input)
                if copies >= 0:
                    break
                print("Copies cannot be negative.")
            except ValueError:
                print("Invalid input! Copies must be an integer.")

        # Price
        while True:
            price_input = input("Enter Price in ₹ (>= 0): ").strip()
            try:
                price = float(price_input)
                if price >= 0:
                    break
                print("Price cannot be negative.")
            except ValueError:
                print("Invalid input! Price must be a number.")

        # Language
        while True:
            language = input("Enter Language: ").strip()
            if language:
                break
            print("Language cannot be empty. Please try again.")

        # Create new record
        new_book = pd.DataFrame([{
            "Book_ID": book_id,
            "Book_Name": book_name,
            "Author": author,
            "Genre": genre,
            "Publication_Year": pub_year,
            "Rating": rating,
            "Available_Copies": copies,
            "Price": price,
            "Language": language
        }])

        df = pd.concat([df, new_book], ignore_index=True)
        save_dataset(df, file_path)

        print("\n[SUCCESS] New Book Added Successfully!")
        print(new_book.to_string(index=False))

        return df

    except Exception as e:
        print(f"\nError while adding book: {e}")
        return df


def update_book(df, file_path=DEFAULT_FILE_PATH):
    """
    DYNAMIC UPDATE BOOK:
    Find book by ID and dynamically update specific or all fields.
    """
    try:
        print_header("UPDATE BOOK DETAILS")
        book_id = input("Enter Book ID of the book to update: ").strip()
        if not book_id:
            print("Book ID cannot be empty.")
            return df

        idx_list = df.index[df["Book_ID"].astype(str).str.lower() == book_id.lower()].tolist()
        if not idx_list:
            print(f"No book found with ID: '{book_id}'")
            return df

        idx = idx_list[0]
        print("\nCurrent Book Details:")
        print(df.loc[[idx]].to_string(index=False))

        editable_cols = [col for col in df.columns if col != "Book_ID"]
        print("\nSelect Field to Update:")
        for i, col in enumerate(editable_cols, 1):
            print(f"{i}. {col} (Current: {df.at[idx, col]})")
        print(f"{len(editable_cols) + 1}. Update All Fields")

        field_choice = input(f"Enter choice (1-{len(editable_cols) + 1}): ").strip()

        if field_choice.isdigit() and 1 <= int(field_choice) <= len(editable_cols):
            target_col = editable_cols[int(field_choice) - 1]
            new_val = input(f"Enter new value for '{target_col}': ").strip()
            if new_val:
                if pd.api.types.is_numeric_dtype(df[target_col]):
                    new_val = float(new_val) if "." in new_val else int(new_val)
                df.at[idx, target_col] = new_val
                save_dataset(df, file_path)
                print(f"[SUCCESS] Updated '{target_col}' successfully!")
        elif field_choice == str(len(editable_cols) + 1):
            for target_col in editable_cols:
                prompt_val = input(f"Enter new {target_col} [Press Enter to keep '{df.at[idx, target_col]}']: ").strip()
                if prompt_val:
                    if pd.api.types.is_numeric_dtype(df[target_col]):
                        prompt_val = float(prompt_val) if "." in prompt_val else int(prompt_val)
                    df.at[idx, target_col] = prompt_val
            save_dataset(df, file_path)
            print("[SUCCESS] All chosen fields updated successfully!")
        else:
            print("Invalid choice.")

        return df

    except Exception as e:
        print(f"\nError updating book: {e}")
        return df


def delete_book(df, file_path=DEFAULT_FILE_PATH):
    """
    DYNAMIC DELETE BOOK:
    Deletes book by ID after confirmation and updates CSV.
    """
    try:
        print_header("DELETE BOOK RECORD")
        book_id = input("Enter Book ID to delete: ").strip()
        if not book_id:
            print("Book ID cannot be empty.")
            return df

        match = df[df["Book_ID"].astype(str).str.lower() == book_id.lower()]
        if match.empty:
            print(f"No book found with ID: '{book_id}'")
            return df

        print("\nBook found:")
        print(match.to_string(index=False))

        confirm = input("\nAre you sure you want to delete this book? (yes/no): ").strip().lower()
        if confirm in ["yes", "y"]:
            df = df[df["Book_ID"].astype(str).str.lower() != book_id.lower()].reset_index(drop=True)
            save_dataset(df, file_path)
            print(f"[SUCCESS] Book '{book_id}' deleted successfully!")
        else:
            print("[INFO] Deletion canceled.")

        return df

    except Exception as e:
        print(f"\nError deleting book: {e}")
        return df


# ============================================================
# EXPORT DATA
# ============================================================

def export_data(df, default_name="exported_library_data.csv"):
    """Dynamically exports any dataframe to CSV."""
    try:
        filename = input(f"\nEnter export filename (default '{default_name}'): ").strip()
        if not filename:
            filename = default_name
        if not filename.endswith(".csv"):
            filename += ".csv"

        df.to_csv(filename, index=False)
        print(f"[SUCCESS] Exported {len(df)} records to '{filename}' successfully!")
    except Exception as e:
        print(f"Error exporting data: {e}")


# ============================================================
# MAIN MENU (DYNAMIC INTERFACE)
# ============================================================

def main_menu():
    """Main interactive execution loop."""
    df, current_file_path = load_dataset()

    if df is None:
        print("\n[STOPPED] Dataset could not be loaded. Please check file path.")
        return

    while True:
        try:
            print("\n")
            print("============================================================")
            print("           LIBRARY BOOK DATA ANALYZER (DYNAMIC)")
            print("                    PDS MICRO PROJECT")
            print("============================================================")
            print(f"Active File: '{current_file_path}' | Books Count: {len(df)}")
            print("-" * 60)

            print("[BROWSING & DISPLAY]")
            print(" 1. Display Books (All / Head / Tail / Sample / Paginated)")
            print(" 2. Library Statistics & Column Overview")

            print("\n[DYNAMIC SEARCHING]")
            print(" 3. Search Book by ID")
            print(" 4. Search Book by Name")
            print(" 5. Search Books by Author")
            print(" 6. Search Books by Genre")
            print(" 7. Search Books by Language")
            print(" 8. Universal Search (Search across ALL columns)")
            print(" 9. Dynamic Column Search (Choose any column)")

            print("\n[DYNAMIC FILTERING & SORTING]")
            print("10. Filter Books by Rating")
            print("11. Dynamic Multi-Column Filter (Any column, operators & ranges)")
            print("12. Dynamic Sort Books (Any column, Ascending / Descending)")

            print("\n[ADVANCED ANALYTICS & VISUALIZATION]")
            print("13. Dynamic NumPy Analysis (All numeric columns & percentiles)")
            print("14. Data Visualization Studio (Standard Dashboard & Chart Builder)")

            print("\n[RECORD MANAGEMENT (CRUD)]")
            print("15. Add New Book (Dynamic Auto-ID Generation)")
            print("16. Update Existing Book Details")
            print("17. Delete Book by ID")

            print("\n[DATASET UTILITIES]")
            print("18. Export Current Dataset to CSV")
            print("19. Reload / Switch CSV Dataset")
            print("20. Exit Program")
            print("=" * 60)

            choice = input("\nEnter your choice (1-20): ").strip()

            if choice == "1":
                display_all_books(df)
            elif choice == "2":
                library_statistics(df)
            elif choice == "3":
                search_by_id(df)
            elif choice == "4":
                search_by_name(df)
            elif choice == "5":
                books_by_author(df)
            elif choice == "6":
                books_by_genre(df)
            elif choice == "7":
                books_by_language(df)
            elif choice == "8":
                universal_search(df)
            elif choice == "9":
                dynamic_column_search(df)
            elif choice == "10":
                filter_by_rating(df)
            elif choice == "11":
                dynamic_filter(df)
            elif choice == "12":
                sort_books(df)
            elif choice == "13":
                numpy_analysis(df)
            elif choice == "14":
                generate_visualizations(df)
            elif choice == "15":
                df = add_book(df, current_file_path)
            elif choice == "16":
                df = update_book(df, current_file_path)
            elif choice == "17":
                df = delete_book(df, current_file_path)
            elif choice == "18":
                export_data(df)
            elif choice == "19":
                new_path = input("Enter CSV path to load (press Enter for default): ").strip()
                new_path = new_path if new_path else DEFAULT_FILE_PATH
                new_df, valid_path = load_dataset(new_path)
                if new_df is not None:
                    df = new_df
                    current_file_path = valid_path
            elif choice in ["20", "exit", "quit"]:
                print("\nThank you for using Library Book Data Analyzer! Goodbye.\n")
                break
            else:
                print("\n[INVALID] Please enter a valid choice between 1 and 20.")

        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Exiting gracefully.")
            break
        except Exception as e:
            print(f"\nUnexpected error in main menu: {e}")


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":
    main_menu()
