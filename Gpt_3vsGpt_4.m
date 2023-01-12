% Code for two spheres in MATLAB

% Define sphere radii
r1 = 1;
r2 = 541.43;

% Create a grid of points for sphere 1
[x1, y1, z1] = sphere(50);

% Scale the points by the sphere radius
x1 = x1 * r1;
y1 = y1 * r1;
z1 = z1 * r1;

% Create a grid of points for sphere 2
[x2, y2, z2] = sphere(50);

% Scale the points by the sphere radius
x2 = x2 * r2;
y2 = y2 * r2;
z2 = z2 * r2;

% Plot the spheres
figure;
hold on;
surf(x1, y1, z1);

alpha(0.5);
surf(x2-542, y2-542, z2);

alpha(0.5);
hold off;

% Add labels to the spheres
legend("GPT-3 (175 billion parameters)", "GPT-4 (r = 100 trillion parameters)")

% Add a title
title("Comparison of Spheres GPT-3 vs GPT-4")
