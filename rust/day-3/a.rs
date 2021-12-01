use std::fs;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let inp = fs::read_to_string("input.txt")?;

    let grid: Vec<Vec<char>> = inp
        .lines()
        .filter(|s| !s.is_empty())
        .map(|line| line.chars().collect())
        .collect();

    let width = grid[0].len();
    let mut count = 0;
    let mut pos = vec![0, 0];

    while pos[0] < grid.len() - 1 {
        pos[0] += 1;
        pos[1] = (pos[1] + 3) % width;

        if grid[pos[0]][pos[1]] == '#' {
            count += 1;
        }
    }

    println!("{}", count);
    Ok(())

}