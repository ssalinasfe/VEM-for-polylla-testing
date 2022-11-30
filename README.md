Scripts I made to test 2D Polylla meshes using the Virtual Element Method (VEM).

## Files

- vem.py: Original VEM code from [here](https://github.com/justachetan/VirtualElementMethods)
- samplesGeneration.ipynb: Notebook to generate samples for the VEM code, this generates 2D meshes with different number of elements and point distributions
    - Random mesh: Mesh with random points in a square domain
    - Poisson mesh: Mesh with points generated using a Poisson disk sampling
    - Uniform mesh: Mesh with points generated using a regular grid
    - SeminUniform mesh: Mesh generated using Triangle with the constrains 'qa[number]'
- vemPolylla.ipynb: Notebook to test the VEM code with the meshes generated in samplesGeneration.ipynb
- divergence.ipynb: Notebook to test the divergence of the VEM code with the meshes generated in samplesGeneration.ipynb

[Original paper of VEM](https://link.springer.com/article/10.1007/s11075-016-0235-3)