def max_polygon_perimeter(nums):
    # Rendisim numrat në rritje
    nums.sort()

    # Përdorim një ndryshore për të ruajtur shumën totale të anëve
    total_sum = sum(nums)

    # Fillojmë duke përdorur të gjithë elementët dhe zvogëlojmë derisa të gjejmë një poligon të vlefshëm
    for i in range(len(nums) - 1, 1, -1):  # Fillojmë nga ana më e gjatë dhe zvogëlojmë
        if total_sum - nums[i] > nums[i]:  # Kontrollojmë nëse mund të krijohet një poligon
            return total_sum  # Kthejmë perimetrin më të madh të mundshëm
        total_sum -= nums[i]  # Hiq anën më të madhe dhe vazhdo

    return -1  # Nëse nuk gjendet poligon i vlefshëm, kthejmë -1


# Testimi me shembujt e dhënë
print(max_polygon_perimeter([5, 5, 5]))  # Output: 15
print(max_polygon_perimeter([1, 12, 1, 2, 5, 50, 3]))  # Output: 12