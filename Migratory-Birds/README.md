# 🐦 Migratory Birds Identifier 🐦

This Python function, `migratoryBirds`, helps identify the most migratory bird type based on a list of bird sightings. It's a simple yet effective way to determine the bird species that has been spotted the most.

## Features 🦉

- **Efficient Algorithm:** The function efficiently counts and identifies the most migratory bird type using Python's list manipulation.

## Usage 🚀

1. **Function Integration:** You can integrate the `migratoryBirds` function into your Python project by copying the code.

2. **Input:** The function takes a list of bird sightings as input, where each sighting is represented by an integer (bird type).

3. **Output:** It returns the type of the most migratory bird as an integer.

4. **Example:**

   ```python
   bird_sightings = [1, 2, 3, 4, 5, 5, 3, 2, 4, 1, 2, 2, 4]
   most_migratory_bird = migratoryBirds(bird_sightings)
   print(f"The most migratory bird type is: {most_migratory_bird}")
   ```

## Algorithm 🧠

The `migratoryBirds` function utilizes a counting mechanism to identify the most migratory bird:

1. It initializes a list `bird_counts` with 6 elements, one for each bird type (types 1 to 5). These elements are used to count the occurrences of each bird type.

2. It loops through the list of bird sightings and increments the corresponding element in `bird_counts` for each sighting.

3. It then finds the maximum count of bird sightings.

4. Finally, it identifies the bird type with the maximum count, which represents the most migratory bird.

## Contributions Welcome 🤝

Contributions are welcome! If you have suggestions for improvements, optimizations, or additional features, please feel free to fork the repository, make your changes, and submit a pull request.

Check out our [Contribution Guidelines](CONTRIBUTING.md) to get started

## Find Us Online 🌐

Discover more exciting coding projects on our [GitHub repository](https://github.com/Maham-j).

Connect with the developer, Maham Jamil, on [LinkedIn](https://www.linkedin.com/in/maham-jamil-268584267).

Connect with the developer, Maham Jamil, on [HackerRank](https://www.hackerrank.com/maham_jamil)

## License 📜

This project is open-source and available under the GNU General Public License v3.0.. See the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by [Maham.J](https://github.com/Maham-j)

If you find this function helpful, show your support by giving it a ⭐️!
