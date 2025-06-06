class InvalidShapeError(Exception):
    """
    Custom exception for invalid Tetromino shapes.
    """
    def __init__(self, message="Invalid shape dimensions or structure."):
        super().__init__(message)


class Shape:
    """
    Class representing a shape in the Tetris game.
    """
    def __init__(self, width, height, shape):
        """
        Initialize a Shape object.
        :param width: The width of the shape.
        :param height: The height of the shape.
        :param shape: A 2D list representing the shape.
        """
        self.width = width
        self.height = height
        self.shape = shape
        if not self.validate():
            raise InvalidShapeError("Shape does not match the given dimensions.")

    def validate(self) -> bool:
        """
        Validate the Tetromino piece.
        :return: True if valid, False otherwise.
        """
        if len(self.shape) != self.height:
            return False
        for row in self.shape:
            if len(row) != self.width:
                return False
        return True

    def rotate(self):
        """
        Return a new Shape object rotated 90 degrees clockwise.
        """
        rotated_shape = [list(row) for row in zip(*self.shape[::-1])]
        return Shape(self.height, self.width, rotated_shape)

    def __repr__(self):
        return f"Shape(width={self.width}, height={self.height}, shape={self.shape})"


class Tetromino:
    """
    General class for Tetromino pieces.
    """
    def __init__(self, shape: Shape, name: str):
        """
        Initialize a Tetromino piece.
        :param shape: A Shape object representing the piece.
        :param name: A string name for the piece (e.g., "L", "T").
        """
        self.shape = shape
        self.name = name

    def rotate_clockwise(self, degrees: int = 90):
        """
        Rotate the Tetromino piece by rotating its shape.
        """
        if degrees % 90 != 0:
            raise ValueError("Rotation degrees must be a multiple of 90.")
        for _ in range(degrees // 90):
            self.shape = self.shape.rotate()

    def get_dimensions(self):
        """
        Get the dimensions of the Tetromino piece.
        :return: A tuple (width, height).
        """
        return self.shape.width, self.shape.height

    def __repr__(self):
        return f"Tetromino(name={self.name}, shape={self.shape})" + self._shape()

    def _shape(self):
        """
        Get the shape of the Tetromino piece.
        :return: The shape of the Tetromino.
        """
        shape_string = ""
        
        for row in self.shape.shape:
            shape_string += "\n" + "".join(str(cell) for cell in row)
            
        return shape_string
