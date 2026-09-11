class Solution {
    public int maxProfit(int[] prices) {
        int buyingIndex = 0;
        int maxProfit = 0;
        for (int sellingIndex = 1; sellingIndex < prices.length; sellingIndex++) {
            int buyingPrice = prices[sellingIndex - 1];
            int ogPrice = prices[buyingIndex];
            System.out.println("Og: " + ogPrice);
            System.out.println("Buy: " + buyingPrice);
            if (ogPrice > buyingPrice) {
                buyingIndex = sellingIndex - 1;
            } else {
                buyingPrice = ogPrice;
            }
            System.out.println(prices[sellingIndex]);
            System.out.println(prices[sellingIndex] - buyingPrice);
            maxProfit = Math.max(maxProfit, prices[sellingIndex] - buyingPrice);
        }
        return maxProfit;
    }
}
