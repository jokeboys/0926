def calculate_cagr(start_price, end_price, years):
    return ((end_price / start_price) ** (1/years)) - 1

start_price = float(input("請輸入起始價格: "))
end_price = float(input("請輸入結束價格: "))
years = float(input("請輸入年份: "))

cagr = calculate_cagr(start_price, end_price, years)

print(f"股票的年度複合成長率為 {cagr * 100:.2f}%")