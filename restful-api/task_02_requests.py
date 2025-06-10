#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from a placeholder API and prints their titles.

    Sends a GET request to 'https://jsonplaceholder.typicode.com/posts'.
    If the request is successful and the response is valid JSON,
    it prints the title of each post.

    Returns:
        None
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        print("Status Code:", r.status_code)
        try:
            data = r.json()
            for i in data:
                print(i["title"])
        except ValueError:
            print("Error: Invalid JSON response")


def fetch_and_save_posts():
    """
    Fetches posts from a placeholder API and saves selected fields to a CSV
    file.

    Sends a GET request to 'https://jsonplaceholder.typicode.com/posts'.
    If the request is successful and the response is valid JSON,
    it extracts 'id', 'title', and 'body' from each post and writes them
    into a file named 'posts.csv'.

    Returns:
        None
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        try:
            data = r.json()

            new_bag = []
            for j in data:
                new_bag.append({
                    "id": j["id"],
                    "title": j["title"],
                    "body": j["body"]
                })

            with open("posts.csv", "w", newline='', encoding="utf-8") as f:
                fieldnames = ["id", "title", "body"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(new_bag)

        except ValueError:
            print("Error: Invalid JSON response")
