price_gpu = 250;
budget = float(input())
gpus = int(input())
cpus = int(input())
rams = int(input())

gpu_price = gpus * price_gpu
cpu_price = gpu_price * 0.35 * cpus
ram_price = gpu_price * 0.1 * rams
whole_price = gpu_price + cpu_price + ram_price
if gpus > cpus:
    whole_price -= (whole_price * 0.15);
if whole_price <= budget:
    print(f'You have {(budget - whole_price):.2f} leva left!')
else:
    print(f'Not enough money! You need {(whole_price - budget):.2f} leva more!')
