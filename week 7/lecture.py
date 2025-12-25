# a = [1, 2, 3, 4, 5]
# a.append(6)
# a.insert(0, 2)
# a.pop(0)
# a.remove(2)


# print(a)
# grid = [[1, 2, 3], [4, 5, 6]]
# # for r in range(len(grid)):
# #     for c in range(len(grid[r])):
# #         print(grid[r][c])
# for row_list in grid:
#     for item in row_list:
#         print(item)
# def find_item_location(warehouse_grid, target_item):
#     for r in range(len(warehouse_grid)):
#         for c in range(len(warehouse_grid[r])):
#             if warehouse_grid[r][c] == target_item:
#                 return (r, c)
#     else:
#         return None
            
# grid = [[101, 102], [201, 202]]
# print(find_item_location(grid, 201))

# # --- Testing the function ---
# warehouse = [[11, 23, 76], [45, 98, 50], [88, 62, 37]]
# print(find_item_location(warehouse, 98))  # Expected output: (1, 1)
# print(find_item_location(warehouse, 100)) # Expected output: None
