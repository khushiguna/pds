# ============================================================
# LIBRARY BOOK DATA ANALYZER
# PDS MICRO PROJECT
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ------------------------------------------------------------
# FILE PATH
# ------------------------------------------------------------

file_path = "library_books.csv"


# ------------------------------------------------------------
# LOAD DATASET
# ------------------------------------------------------------

try:
    df = pd.read_csv(file_path)

    print("\n================================================")
    print("       LIBRARY BOOK DATA ANALYZER")
    print("================================================")
    print("\nDataset loaded successfully.")
    print("Total records:", len(df))

except FileNotFoundError:
    print("\nError: library_books.csv file not found.")
    print("Please check the 'data' folder and file name.")

except Exception as e:
    print("\nError while loading dataset:", e)


finally:
    print("Dataset loading process completed.")


# ------------------------------------------------------------
# DISPLAY ALL BOOKS
# ------------------------------------------------------------

def display_all_books():

    try:
        if df.empty:
            print("\nNo books available.")
            return

        print("\n================ ALL BOOKS ================\n")
        print(df.to_string(index=False))
        print("\nTotal Books:", len(df))

    except Exception as e:
        print("Error:", e)

    finally:
        print("\nDisplay operation completed.")


# ------------------------------------------------------------
# ADD NEW BOOK
# ------------------------------------------------------------

def add_book():

    global df

    try:
        print("\n================ ADD NEW BOOK ================\n")

        # Book ID
        book_id = input("Enter Book ID: ").strip()

        if book_id == "":
            print("Book ID cannot be empty.")
            return

        if book_id in df["Book_ID"].astype(str).values:
            print("Book ID already exists.")
            return

        # Book Name
        book_name = input("Enter Book Name: ").strip()

        if book_name == "":
            print("Book Name cannot be empty.")
            return

        # Author
        author = input("Enter Author Name: ").strip()

        if author == "":
            print("Author name cannot be empty.")
            return

        # Genre
        genre = input("Enter Genre: ").strip()

        if genre == "":
            print("Genre cannot be empty.")
            return

        # Publication Year
        publication_year = int(input("Enter Publication Year: "))

        if publication_year < 1900 or publication_year > 2100:
            print("Enter a valid publication year.")
            return

        # Rating
        rating = float(input("Enter Rating (0-5): "))

        if rating < 0 or rating > 5:
            print("Rating must be between 0 and 5.")
            return

        # Available Copies
        available_copies = int(input("Enter Available Copies: "))

        if available_copies < 0:
            print("Available copies cannot be negative.")
            return

        # Price
        price = float(input("Enter Price: "))

        if price < 0:
            print("Price cannot be negative.")
            return

        # Language
        language = input("Enter Language: ").strip()

        if language == "":
            print("Language cannot be empty.")
            return

        # Create new record
        new_book = pd.DataFrame({
            "Book_ID": [book_id],
            "Book_Name": [book_name],
            "Author": [author],
            "Genre": [genre],
            "Publication_Year": [publication_year],
            "Rating": [rating],
            "Available_Copies": [available_copies],
            "Price": [price],
            "Language": [language]
        })

        # Add record
        df = pd.concat([df, new_book], ignore_index=True)

        # Save updated dataset
        df.to_csv(file_path, index=False)

        print("\nBook added successfully!")
        print("\nNew Book Details:")
        print(new_book.to_string(index=False))

    except ValueError:
        print("\nInvalid input!")
        print("Please enter numbers correctly for year, rating, copies and price.")

    except Exception as e:
        print("\nError while adding book:", e)

    finally:
        print("\nAdd book operation completed.")


# ------------------------------------------------------------
# SEARCH BOOK BY ID
# ------------------------------------------------------------

def search_by_id():

    try:
        book_id = input("\nEnter Book ID: ").strip()

        result = df[df["Book_ID"].astype(str) == book_id]

        if result.empty:
            print("\nNo book found with this Book ID.")

        else:
            print("\n================ BOOK DETAILS ================\n")
            print(result.to_string(index=False))

    except Exception as e:
        print("\nError:", e)

    finally:
        print("\nSearch operation completed.")


# ------------------------------------------------------------
# SEARCH BOOK BY NAME
# ------------------------------------------------------------

def search_by_name():

    try:
        name = input("\nEnter Book Name: ").strip()

        result = df[
            df["Book_Name"]
            .astype(str)
            .str.contains(name, case=False, na=False)
        ]

        if result.empty:
            print("\nNo book found.")

        else:
            print("\n================ SEARCH RESULT ================\n")
            print(result.to_string(index=False))
            print("\nBooks Found:", len(result))

    except Exception as e:
        print("\nError:", e)

    finally:
        print("\nBook name search completed.")


# ------------------------------------------------------------
# SEARCH BOOKS BY AUTHOR
# ------------------------------------------------------------

def books_by_author():

    try:
        author = input("\nEnter Author Name: ").strip()

        result = df[
            df["Author"]
            .astype(str)
            .str.lower() == author.lower()
        ]

        if result.empty:
            print("\nNo books found for this author.")

        else:
            print("\n============================================")
            print("Books written by:", author)
            print("============================================\n")

            print(result.to_string(index=False))

            print("\nTotal books by this author:", len(result))

    except Exception as e:
        print("\nError:", e)

    finally:
        print("\nAuthor search completed.")


# ------------------------------------------------------------
# SEARCH BOOKS BY GENRE
# ------------------------------------------------------------

def books_by_genre():

    try:
        genre = input("\nEnter Genre: ").strip()

        result = df[
            df["Genre"]
            .astype(str)
            .str.lower() == genre.lower()
        ]

        if result.empty:
            print("\nNo books found in this genre.")

        else:
            print("\n================ GENRE BOOKS ================\n")
            print(result.to_string(index=False))
            print("\nTotal books in this genre:", len(result))

    except Exception as e:
        print("\nError:", e)

    finally:
        print("\nGenre search completed.")


# ------------------------------------------------------------
# SEARCH BOOKS BY LANGUAGE
# ------------------------------------------------------------

def books_by_language():

    try:
        language = input("\nEnter Language: ").strip()

        result = df[
            df["Language"]
            .astype(str)
            .str.lower() == language.lower()
        ]

        if result.empty:
            print("\nNo books found for this language.")

        else:
            print("\n================ LANGUAGE BOOKS ================\n")
            print(result.to_string(index=False))
            print("\nTotal books:", len(result))

    except Exception as e:
        print("\nError:", e)

    finally:
        print("\nLanguage search completed.")


# ------------------------------------------------------------
# UPDATE BOOK
# ------------------------------------------------------------

def update_book():

    global df

    try:
        print("\n================ UPDATE BOOK ================\n")

        book_id = input("Enter Book ID to update: ").strip()

        index = df.index[
            df["Book_ID"].astype(str) == book_id
        ].tolist()

        if len(index) == 0:
            print("\nBook not found.")
            return

        index = index[0]

        print("\nCurrent Book Details:")
        print(df.loc[[index]].to_string(index=False))

        print("\nEnter new details.")

        book_name = input("Enter new Book Name: ").strip()
        author = input("Enter new Author: ").strip()
        genre = input("Enter new Genre: ").strip()

        publication_year = int(
            input("Enter new Publication Year: ")
        )

        rating = float(
            input("Enter new Rating (0-5): ")
        )

        available_copies = int(
            input("Enter new Available Copies: ")
        )

        price = float(
            input("Enter new Price: ")
        )

        language = input("Enter new Language: ").strip()

        if rating < 0 or rating > 5:
            print("Rating must be between 0 and 5.")
            return

        if available_copies < 0:
            print("Available copies cannot be negative.")
            return

        if price < 0:
            print("Price cannot be negative.")
            return

        # Update values
        df.loc[index, "Book_Name"] = book_name
        df.loc[index, "Author"] = author
        df.loc[index, "Genre"] = genre
        df.loc[index, "Publication_Year"] = publication_year
        df.loc[index, "Rating"] = rating
        df.loc[index, "Available_Copies"] = available_copies
        df.loc[index, "Price"] = price
        df.loc[index, "Language"] = language

        # Save changes
        df.to_csv(file_path, index=False)

        print("\nBook updated successfully!")

        print("\nUpdated Details:")
        print(df.loc[[index]].to_string(index=False))

    except ValueError:
        print("\nInvalid input! Please enter correct numeric values.")

    except Exception as e:
        print("\nError while updating:", e)

    finally:
        print("\nUpdate operation completed.")


# ------------------------------------------------------------
# DELETE BOOK
# ------------------------------------------------------------

def delete_book():

    global df

    try:
        print("\n================ DELETE BOOK ================\n")

        book_id = input("Enter Book ID to delete: ").strip()

        result = df[
            df["Book_ID"].astype(str) == book_id
        ]

        if result.empty:
            print("\nBook not found.")
            return

        print("\nBook to be deleted:")
        print(result.to_string(index=False))

        confirm = input(
            "\nAre you sure you want to delete this book? (y/n): "
        ).lower()

        if confirm == "y":

            df = df[
                df["Book_ID"].astype(str) != book_id
            ]

            df.to_csv(file_path, index=False)

            print("\nBook deleted successfully.")

        else:
            print("\nDelete operation cancelled.")

    except Exception as e:
        print("\nError while deleting:", e)

    finally:
        print("\nDelete operation completed.")


# ------------------------------------------------------------
# LIBRARY STATISTICS
# ------------------------------------------------------------

def library_statistics():

    try:
        print("\n================================================")
        print("              LIBRARY STATISTICS")
        print("================================================")

        total_books = len(df)

        total_authors = df["Author"].nunique()

        total_genres = df["Genre"].nunique()

        average_rating = df["Rating"].mean()

        total_copies = df["Available_Copies"].sum()

        average_price = df["Price"].mean()

        print("\nTotal Books:", total_books)
        print("Total Authors:", total_authors)
        print("Total Genres:", total_genres)
        print("Average Rating:", round(average_rating, 2))
        print("Total Available Copies:", total_copies)
        print("Average Book Price:", round(average_price, 2))

        print("\nGenre Count:")
        print(df["Genre"].value_counts())

        print("\nAuthor Count:")
        print(df["Author"].value_counts())

    except Exception as e:
        print("\nError:", e)

    finally:
        print("\nStatistics operation completed.")


# ------------------------------------------------------------
# RATING AND PRICE ANALYSIS
# ------------------------------------------------------------

def rating_price_analysis():

    try:
        print("\n================================================")
        print("           RATING AND PRICE ANALYSIS")
        print("================================================")

        highest_rating = df["Rating"].max()
        lowest_rating = df["Rating"].min()

        print("\nHighest Rating:", highest_rating)
        print("Lowest Rating:", lowest_rating)

        highest_rated = df[
            df["Rating"] == highest_rating
        ]

        print("\nHighest Rated Book(s):")
        print(
            highest_rated[
                ["Book_Name", "Author", "Rating"]
            ].to_string(index=False)
        )

        lowest_rated = df[
            df["Rating"] == lowest_rating
        ]

        print("\nLowest Rated Book(s):")
        print(
            lowest_rated[
                ["Book_Name", "Author", "Rating"]
            ].to_string(index=False)
        )

        expensive = df["Price"].max()

        cheapest = df["Price"].min()

        print("\nMost Expensive Price:", expensive)
        print("Cheapest Price:", cheapest)

        print("\nMost Expensive Book:")
        print(
            df[df["Price"] == expensive][
                ["Book_Name", "Price"]
            ].to_string(index=False)
        )

        print("\nCheapest Book:")
        print(
            df[df["Price"] == cheapest][
                ["Book_Name", "Price"]
            ].to_string(index=False)
        )

    except Exception as e:
        print("\nError:", e)

    finally:
        print("\nRating and price analysis completed.")


# ------------------------------------------------------------
# ADVANCED ANALYSIS
# ------------------------------------------------------------

def advanced_analysis():

    try:
        print("\n================================================")
        print("              ADVANCED ANALYSIS")
        print("================================================")

        print("\nAverage Rating by Genre:")

        genre_rating = df.groupby(
            "Genre"
        )["Rating"].mean().sort_values(ascending=False)

        print(genre_rating.round(2))

        print("\nAvailable Copies by Genre:")

        genre_copies = df.groupby(
            "Genre"
        )["Available_Copies"].sum().sort_values(
            ascending=False
        )

        print(genre_copies)

        print("\nPublication Year Count:")

        year_count = df["Publication_Year"].value_counts().sort_index()

        print(year_count)

        print("\nTop 10 Authors:")

        top_authors = df["Author"].value_counts().head(10)

        print(top_authors)

    except Exception as e:
        print("\nError:", e)

    finally:
        print("\nAdvanced analysis completed.")


# ------------------------------------------------------------
# NUMPY ANALYSIS
# ------------------------------------------------------------

def numpy_analysis():

    try:
        print("\n================================================")
        print("                NUMPY ANALYSIS")
        print("================================================")

        ratings = np.array(df["Rating"])

        prices = np.array(df["Price"])

        print("\nRating Analysis using NumPy")

        print("Maximum Rating:", np.max(ratings))
        print("Minimum Rating:", np.min(ratings))
        print("Average Rating:", round(np.mean(ratings), 2))

        print("\nPrice Analysis using NumPy")

        print("Maximum Price:", np.max(prices))
        print("Minimum Price:", np.min(prices))
        print("Average Price:", round(np.mean(prices), 2))

    except Exception as e:
        print("\nError:", e)

    finally:
        print("\nNumPy analysis completed.")


# ------------------------------------------------------------
# FILTER BOOKS BY RATING
# ------------------------------------------------------------

def filter_by_rating():

    try:
        rating = float(
            input("\nEnter minimum rating: ")
        )

        if rating < 0 or rating > 5:
            print("Rating must be between 0 and 5.")
            return

        result = df[
            df["Rating"] >= rating
        ].sort_values(
            by="Rating",
            ascending=False
        )

        if result.empty:
            print("\nNo books found.")

        else:
            print(
                "\nBooks with rating >= ",
                rating
            )

            print(
                result.to_string(index=False)
            )

            print("\nTotal books:", len(result))

    except ValueError:
        print("\nPlease enter a valid number.")

    except Exception as e:
        print("\nError:", e)

    finally:
        print("\nRating filter operation completed.")


# ------------------------------------------------------------
# SORT BOOKS
# ------------------------------------------------------------

def sort_books():

    try:
        print("\n================ SORT BOOKS ================")

        print("1. Sort by Book Name")
        print("2. Sort by Rating")
        print("3. Sort by Price")
        print("4. Sort by Publication Year")
        print("5. Sort by Available Copies")

        choice = input("\nEnter your choice: ")

        columns = {
            "1": "Book_Name",
            "2": "Rating",
            "3": "Price",
            "4": "Publication_Year",
            "5": "Available_Copies"
        }

        if choice not in columns:
            print("\nInvalid choice.")
            return

        column = columns[choice]

        result = df.sort_values(
            by=column,
            ascending=True
        )

        print(
            "\nBooks sorted by",
            column,
            ":\n"
        )

        print(result.to_string(index=False))

    except Exception as e:
        print("\nError:", e)

    finally:
        print("\nSorting operation completed.")


# ------------------------------------------------------------
# VISUALIZATION
# ------------------------------------------------------------

def generate_visualizations():

    try:
        print("\nGenerating visualizations...")

        # 1. Genre Count
        genre_count = df["Genre"].value_counts()

        plt.figure(figsize=(10, 5))

        genre_count.plot(
            kind="bar"
        )

        plt.title("Number of Books by Genre")
        plt.xlabel("Genre")
        plt.ylabel("Number of Books")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


        # 2. Publication Year
        year_count = df[
            "Publication_Year"
        ].value_counts().sort_index()

        plt.figure(figsize=(10, 5))

        plt.plot(
            year_count.index,
            year_count.values,
            marker="o"
        )

        plt.title("Books by Publication Year")
        plt.xlabel("Publication Year")
        plt.ylabel("Number of Books")
        plt.grid(True)
        plt.tight_layout()
        plt.show()


        # 3. Rating Distribution
        plt.figure(figsize=(8, 5))

        sns.histplot(
            df["Rating"],
            bins=10,
            kde=True
        )

        plt.title("Rating Distribution")
        plt.xlabel("Rating")
        plt.ylabel("Number of Books")
        plt.tight_layout()
        plt.show()


        # 4. Top 10 Authors
        top_authors = df[
            "Author"
        ].value_counts().head(10)

        plt.figure(figsize=(10, 5))

        top_authors.plot(
            kind="bar"
        )

        plt.title("Top 10 Authors")
        plt.xlabel("Author")
        plt.ylabel("Number of Books")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


        # 5. Average Rating by Genre
        avg_rating = df.groupby(
            "Genre"
        )["Rating"].mean()

        plt.figure(figsize=(10, 5))

        avg_rating.plot(
            kind="bar"
        )

        plt.title("Average Rating by Genre")
        plt.xlabel("Genre")
        plt.ylabel("Average Rating")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


        # 6. Available Copies by Genre
        copies = df.groupby(
            "Genre"
        )["Available_Copies"].sum()

        plt.figure(figsize=(10, 5))

        copies.plot(
            kind="bar"
        )

        plt.title("Available Copies by Genre")
        plt.xlabel("Genre")
        plt.ylabel("Available Copies")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        print("\nAll visualizations generated successfully.")

    except Exception as e:
        print("\nError while generating visualization:", e)

    finally:
        print("\nVisualization operation completed.")


# ------------------------------------------------------------
# DASHBOARD
# ------------------------------------------------------------

def generate_dashboard():

    try:
        print("\nGenerating dashboard...")

        total_books = len(df)

        average_rating = df["Rating"].mean()

        total_genres = df["Genre"].nunique()

        total_authors = df["Author"].nunique()

        genre_count = df["Genre"].value_counts()

        year_count = (
            df["Publication_Year"]
            .value_counts()
            .sort_index()
        )

        top_authors = (
            df["Author"]
            .value_counts()
            .head(10)
        )

        avg_rating = (
            df.groupby("Genre")["Rating"]
            .mean()
            .sort_values(
                ascending=False
            )
        )


        plt.figure(
            figsize=(15, 10)
        )

        plt.suptitle(
            "LIBRARY BOOK DATA ANALYZER DASHBOARD",
            fontsize=20,
            fontweight="bold"
        )


        # -------------------------------
        # Chart 1
        # -------------------------------

        plt.subplot(2, 2, 1)

        genre_count.plot(
            kind="bar"
        )

        plt.title("Books by Genre")
        plt.xlabel("Genre")
        plt.ylabel("Number of Books")
        plt.xticks(rotation=45)


        # -------------------------------
        # Chart 2
        # -------------------------------

        plt.subplot(2, 2, 2)

        plt.plot(
            year_count.index,
            year_count.values,
            marker="o"
        )

        plt.title("Books by Publication Year")
        plt.xlabel("Year")
        plt.ylabel("Number of Books")


        # -------------------------------
        # Chart 3
        # -------------------------------

        plt.subplot(2, 2, 3)

        top_authors.plot(
            kind="bar"
        )

        plt.title("Top 10 Authors")
        plt.xlabel("Author")
        plt.ylabel("Number of Books")
        plt.xticks(rotation=45)


        # -------------------------------
        # Chart 4
        # -------------------------------

        plt.subplot(2, 2, 4)

        avg_rating.plot(
            kind="bar"
        )

        plt.title("Average Rating by Genre")
        plt.xlabel("Genre")
        plt.ylabel("Average Rating")
        plt.xticks(rotation=45)


        # Dashboard information
        plt.figtext(
            0.02,
            0.02,
            "Total Books: "
            + str(total_books)
            + "     |     Average Rating: "
            + str(round(average_rating, 2))
            + "     |     Total Genres: "
            + str(total_genres)
            + "     |     Total Authors: "
            + str(total_authors),
            fontsize=12
        )

        plt.tight_layout(
            rect=[0, 0.05, 1, 0.95]
        )

        plt.savefig(
            "library_dashboard.png",
            dpi=300
        )

        plt.show()

        print(
            "\nDashboard saved as "
            "'library_dashboard.png'"
        )

    except Exception as e:
        print("\nError while creating dashboard:", e)

    finally:
        print("\nDashboard operation completed.")


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------

def main_menu():

    while True:

        try:

            print("\n")
            print("================================================")
            print("       LIBRARY BOOK DATA ANALYZER")
            print("================================================")

            print("\n1.  Display All Books")
            print("2.  Add New Book")
            print("3.  Search Book by ID")
            print("4.  Search Book by Name")
            print("5.  Display Books by Author")
            print("6.  Display Books by Genre")
            print("7.  Display Books by Language")
            print("8.  Update Book")
            print("9.  Delete Book")
            print("10. Library Statistics")
            print("11. Rating and Price Analysis")
            print("12. Advanced Analysis")
            print("13. NumPy Analysis")
            print("14. Filter Books by Rating")
            print("15. Sort Books")
            print("16. Generate Visualizations")
            print("17. Generate Dashboard")
            print("18. Exit")

            choice = input(
                "\nEnter your choice: "
            )

            if choice == "1":
                display_all_books()

            elif choice == "2":
                add_book()

            elif choice == "3":
                search_by_id()

            elif choice == "4":
                search_by_name()

            elif choice == "5":
                books_by_author()

            elif choice == "6":
                books_by_genre()

            elif choice == "7":
                books_by_language()

            elif choice == "8":
                update_book()

            elif choice == "9":
                delete_book()

            elif choice == "10":
                library_statistics()

            elif choice == "11":
                rating_price_analysis()

            elif choice == "12":
                advanced_analysis()

            elif choice == "13":
                numpy_analysis()

            elif choice == "14":
                filter_by_rating()

            elif choice == "15":
                sort_books()

            elif choice == "16":
                generate_visualizations()

            elif choice == "17":
                generate_dashboard()

            elif choice == "18":
                print("\nThank you for using Library Book Data Analyzer.")
                break

            else:
                print("\nInvalid choice!")
                print("Please enter a number from 1 to 18.")

        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            break

        except Exception as e:
            print("\nUnexpected error:", e)

        finally:
            print("\n--------------------------------------------")


# ------------------------------------------------------------
# START PROGRAM
# ------------------------------------------------------------

main_menu()
