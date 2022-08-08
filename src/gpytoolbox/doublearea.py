import numpy as np
from gpytoolbox.halfedge_lengths_squared import halfedge_lengths_squared
from gpytoolbox.edge_indices import edge_indices
from gpytoolbox.doublearea_intrinsic import doublearea_intrinsic

def doublearea(V,F=None):
    """Construct the doublearea of each element of a line or triangle mesh.

    Parameters
    ----------
    V : (n,d) numpy array
        vertex list of a polyline or triangle mesh
    F : numpy int array, optional (default: None)
        if None or (m,2), interpret input as ordered polyline;
        if (m,3) numpy int array, interpred as face index list of a triangle
        mesh

    Returns
    -------
    dblA : (m,) numpy double array
        vector of twice the (unsigned) area/length 

    See Also
    --------
    doublearea_intrinsic.

    Examples
    --------
    TO-DO
    """

    # if you didn't pass an F then this is a ordered polyline
    if (F is None):
        F = edge_indices(V.shape[0])

    simplex_size = F.shape[1]
    # Option 1: simplex size is two
    if simplex_size==2:
        # Then this is just finite difference with varying edge lengths
        A = np.linalg.norm(V[F[:,1],:] - V[F[:,0],:],axis=1)
        dblA = 2.0*A
        
    if simplex_size==3:
        l_sq = halfedge_lengths_squared(V,F)
        dblA = doublearea_intrinsic(l_sq,F)

    return dblA
