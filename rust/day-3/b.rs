use std::fs;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let inp = fs::read_to_string("input.txt")?;

    let grid: Vec<Vec<char>> = inp
        .lines()
        .filter(|s| !s.is_empty())
        .map(|line| line.chars().collect())
        .collect();
    
    let slopes: Vec<(usize, usize)> = vec![(1,1), (1,3), (1,5), (1,7), (2,1)];
    let product: usize = slopes
        .iter()
        .map(|s| trees_hit(&grid, s))
        .product();
    
    println!("{}", product);

    Ok(())
}

fn trees_hit(grid: &Vec<Vec<char>>, slope: &(usize, usize)) -> usize {
    let d_x = slope.1;
    let d_y = slope.0;
    let height = grid.len();
    let width = grid[0].len();
    
    let mut count = 0;
    let mut pos: Vec<usize> = vec![0, 0];

    while pos[0] < height - 1 {
        pos[0] += d_y;
        pos[1] = (pos[1] + d_x) % width;
    
        if pos[0] < height && grid[pos[0]][pos[1]] == '#' {
            count += 1;
        }
    }

    count
}