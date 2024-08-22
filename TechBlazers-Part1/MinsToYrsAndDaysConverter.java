public class MinsToYrsAndDaysConverter {
    public static void main(String[] args) {
        long minutes = 1_000_000_000L;
        long[] result = minsToYearsAndDays(minutes);

        System.out.println("Years: " + result[0] + ", Days: " + result[1]);
    }

    public static long[] minsToYearsAndDays(long minutes) {
        long totalDays = minutes / 1440;
        long noOfYears = totalDays / 365;
        long noOfDays = totalDays % 365;

        return new long[]{noOfYears, noOfDays};
    }
}
