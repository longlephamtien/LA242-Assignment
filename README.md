# LA242-Assignment

## Overview
This project is a collection of scripts and tools for visualizing and analyzing 3D geometric objects, including cubes, buckyballs, and 3D models of a fawn. The project demonstrates the use of Python for 3D transformations, projections, and plotting using libraries like `matplotlib` and `numpy`.

## Features
- **3D Cube Visualization**: Rotate and project a cube in 2D and 3D.
- **Buckyball Visualization**: Generate and visualize a buckyball (C60 molecule) in 3D and its 2D projection.
- **Fawn 3D Model Visualization**: Load and visualize a 3D model of a fawn, including edges and projections.
- **Custom Rotation**: Apply custom rotation matrices to objects for visualization.

## Requirements
- Python 3.10 or higher
- Required Python libraries:
  - `numpy`
  - `matplotlib`
  - `scipy`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/longlephamtien/LA242-Assignment.git
   cd LA242-Assignment
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the main script to visualize the objects:
```bash
python lab09.py
```

### Key Files
- `lab09.py`: Main script containing the visualization logic.
- `rotation.py`: Provides functions for generating rotation matrices.
- `bucky.py`: Generates vertices and edges for a buckyball.
- `v.mat` and `f.mat`: Data files containing vertices and faces for the 3D fawn model.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- The project uses `matplotlib` for plotting and `numpy` for numerical computations.
- The 3D fawn model is loaded from `.mat` files using `scipy.io`.

## Contact
For any questions or issues, please contact the author at lephamtienlong.4754@gmail.com.