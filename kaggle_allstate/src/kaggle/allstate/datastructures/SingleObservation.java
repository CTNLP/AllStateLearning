/**
 * 
 */
package kaggle.allstate.datastructures;
import java.util.HashMap;
import java.util.Map;
/**
 * @author Christoph Teichmann
 * created Mar 22, 2014 9:41:59 AM
 * @version 0.1
 */
public class SingleObservation
{
	/**
	 * 
	 */
	private final String c;
	/**
	 * 
	 */
	private final String b;
	/**
	 * 
	 */
	private final String a;
	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	@Override
	public String toString()
	{
		StringBuilder builder = new StringBuilder();
		builder.append("SingleObservation [c=");
		builder.append(c);
		builder.append(", b=");
		builder.append(b);
		builder.append(", a=");
		builder.append(a);
		builder.append(", durationPrevious=");
		builder.append(durationPrevious);
		builder.append(", cPrevious=");
		builder.append(cPrevious);
		builder.append(", married=");
		builder.append(married);
		builder.append(", ageYoungest=");
		builder.append(ageYoungest);
		builder.append(", ageOldest=");
		builder.append(ageOldest);
		builder.append(", riskFactor=");
		builder.append(riskFactor);
		builder.append(", carValue=");
		builder.append(carValue);
		builder.append(", carAge=");
		builder.append(carAge);
		builder.append(", homeOwner=");
		builder.append(homeOwner);
		builder.append(", groupSize=");
		builder.append(groupSize);
		builder.append(", location=");
		builder.append(location);
		builder.append(", state=");
		builder.append(state);
		builder.append(", MINUTES_IN_A_DAY=");
		builder.append(MINUTES_IN_A_DAY);
		builder.append(", minutesSinceZero=");
		builder.append(minutesSinceZero);
		builder.append(", day=");
		builder.append(day);
		builder.append(", isSale=");
		builder.append(isSale);
		builder.append(", shoppingPointnumber=");
		builder.append(shoppingPointnumber);
		builder.append(", d=");
		builder.append(d);
		builder.append(", e=");
		builder.append(e);
		builder.append(", f=");
		builder.append(f);
		builder.append(", g=");
		builder.append(g);
		builder.append(", cost=");
		builder.append(cost);
		builder.append("]");
		return builder.toString();
	}
	/**
	 * 
	 */
	private final String durationPrevious;
	/**
	 * 
	 */
	private final String cPrevious;
	/**
	 * 
	 */
	private final boolean married;
	/**
	 * 
	 */
	private final int ageYoungest;
	/**
	 * 
	 */
	private final int ageOldest;
	/**
	 * 
	 */
	private final String riskFactor;
	/**
	 * 
	 */
	private final String carValue;
	/**
	 * 
	 */
	private final int carAge;
	/**
	 * 
	 */
	private static final String TRUE = "1";
	/**
	 * 
	 */
	private final boolean homeOwner;
	/**
	 * 
	 */
	private final int groupSize;
	/**
	 * 
	 */
	private final String location;
	/**
	 * 
	 */
	private final static Map<String,String> STRING_SELFIE = new HashMap<String, String>();
	/**
	 * 
	 */
	private final String state;
	/**
	 * 
	 */
	private final int MINUTES_IN_A_DAY = 24*60;
	/**
	 * 
	 */
	private final int minutesSinceZero;
	/**
	 * 
	 */
	private final String day;
	/**
	 * 
	 */
	private final boolean isSale;
	/**
	 * 
	 */
	private final int shoppingPointnumber;
	/**
	 * 
	 */
	private final String d;
	/**
	 * 
	 */
	private final String e;
	/**
	 * 
	 */
	private final String f;
	/**
	 * 
	 */
	private final String g;
	/**
	 * 
	 */
	private final int cost;
	/**
	 * 
	 * @param parts
	 */
	public SingleObservation(String[] parts)
	{
		this.shoppingPointnumber = Integer.parseInt(parts[1]);
		this.isSale = parts[2].trim().equals(TRUE);
		this.day = makeSafeCopy(parts, 3);
		String[] timeParts = parts[4].split(":");
		this.minutesSinceZero =
						(Integer.parseInt(timeParts[0].trim())*60)+(Integer.parseInt(timeParts[1].trim()));
		this.state = makeSafeCopy(parts, 5);
		this.location = makeSafeCopy(parts, 6);
		this.groupSize = Integer.parseInt(parts[7]);
		this.homeOwner = parts[8].trim().equals(TRUE);
		this.carAge = Integer.parseInt(parts[9]);
		this.carValue = makeSafeCopy(parts, 10);
		this.riskFactor = makeSafeCopy(parts, 11);
		this.ageOldest = Integer.parseInt(parts[12]);
		this.ageYoungest = Integer.parseInt(parts[13]);
		this.married = parts[14].trim().equals(TRUE);
		this.cPrevious = makeSafeCopy(parts, 15);
		this.durationPrevious = makeSafeCopy(parts,16);
		this.a = makeSafeCopy(parts, 17);
		this.b = makeSafeCopy(parts, 18);
		this.c = makeSafeCopy(parts, 19);
		this.d = makeSafeCopy(parts, 20);
		this.e = makeSafeCopy(parts, 21);
		this.f = makeSafeCopy(parts, 22);
		this.g = makeSafeCopy(parts, 23);
		this.cost = Integer.parseInt(parts[24]);
	}
	/**
	 *
	 * @param parts
	 * @return
	 */
	public static String makeSafeCopy(String[] parts, int pos)
	{
		String dprev = parts[pos].trim();
		String dp = STRING_SELFIE.get(dprev);
		if(dp == null)
		{
			dp = new String(dprev);
			STRING_SELFIE.put(dp, dp);
		}
		return dp;
	}
	/**
	 * @return the cost
	 */
	public int getCost()
	{
		return cost;
	}
	/**
	 * @return the c
	 */
	public String getC()
	{
		return c;
	}
	/**
	 * @return the b
	 */
	public String getB()
	{
		return b;
	}
	/**
	 * @return the a
	 */
	public String getA()
	{
		return a;
	}
	/**
	 * @return the durationPrevious
	 */
	public String getDurationPrevious()
	{
		return durationPrevious;
	}
	/**
	 * @return the cPrevious
	 */
	public String getcPrevious()
	{
		return cPrevious;
	}
	/**
	 * @return the married
	 */
	public boolean isMarried()
	{
		return married;
	}
	/**
	 * @return the ageYoungest
	 */
	public int getAgeYoungest()
	{
		return ageYoungest;
	}
	/**
	 * @return the ageOldest
	 */
	public int getAgeOldest()
	{
		return ageOldest;
	}
	/**
	 * @return the riskFactor
	 */
	public String getRiskFactor()
	{
		return riskFactor;
	}
	/**
	 * @return the carValue
	 */
	public String getCarValue()
	{
		return carValue;
	}
	/**
	 * @return the carAge
	 */
	public int getCarAge()
	{
		return carAge;
	}
	/**
	 * @return the true
	 */
	public static String getTrue()
	{
		return TRUE;
	}
	/**
	 * @return the homeOwner
	 */
	public boolean isHomeOwner()
	{
		return homeOwner;
	}
	/**
	 * @return the groupSize
	 */
	public int getGroupSize()
	{
		return groupSize;
	}
	/**
	 * @return the location
	 */
	public String getLocation()
	{
		return location;
	}
	/**
	 * @return the state
	 */
	public String getState()
	{
		return state;
	}
	/**
	 * @return the mINUTES_IN_A_DAY
	 */
	public int getMINUTES_IN_A_DAY()
	{
		return MINUTES_IN_A_DAY;
	}
	/**
	 * @return the minutesSinceZero
	 */
	public int getMinutesSinceZero()
	{
		return minutesSinceZero;
	}
	/**
	 * @return the day
	 */
	public String getDay()
	{
		return day;
	}
	/**
	 * @return the isSale
	 */
	public boolean isSale()
	{
		return isSale;
	}
	/**
	 * @return the shoppingPointnumber
	 */
	public int getShoppingPointnumber()
	{return shoppingPointnumber;}
	/**
	 * @return the d
	 */
	public String getD()
	{return d;}
	/**
	 * @return the e
	 */
	public String getE()
	{return e;}
	/**
	 * @return the f
	 */
	public String getF()
	{return f;}
	/**
	 * @return the g
	 */
	public String getG()
	{return g;}
	/**
	 *
	 * @param second
	 * @param weights
	 * @return
	 */
	public double makeRDF(SingleObservation second, double[] weights, double[] es)
	{
		int pos = 0;
		double val = 0.0;
		val += makeRDF(this.getDay(),second.getDay(),weights,es,pos++);
		val += makeRDF(makeTimeDistance(this.getMinutesSinceZero(),second.getMinutesSinceZero()), weights, es, pos++);
		val += makeRDF(this.getState(), second.getState(), weights, es, pos++);
		val += makeRDF(this.getLocation(), second.getLocation(), weights, es, pos++);
		val += makeRDF(this.getGroupSize()-second.getGroupSize(), weights, es, pos++);
		val += makeRDF(this.isHomeOwner(), second.isHomeOwner(), weights, es, pos++);
		val += makeRDF(this.getCarAge()-second.getCarAge(), weights, es, pos++);
		val += makeRDF(this.getCarValue(),second.getCarValue(), weights, es, pos++);
		val += makeRDF(this.getRiskFactor(),second.getRiskFactor(), weights, es, pos++);
		val += makeRDF(this.getAgeOldest()-second.getAgeOldest(), weights, es, pos++);
		val += makeRDF(this.getAgeYoungest()-second.getAgeYoungest(), weights, es, pos++);
		val += makeRDF(this.isMarried(), second.isMarried(), weights, es, pos++);
		val += makeRDF(this.getcPrevious(),second.getcPrevious(), weights, es, pos++);
		val += makeRDF(this.getDurationPrevious(),second.getDurationPrevious(), weights, es, pos++);
		val += makeRDF(this.getA(),second.getA(), weights, es, pos++);
		val += makeRDF(this.getB(),second.getB(), weights, es, pos++);
		val += makeRDF(this.getC(),second.getC(), weights, es, pos++);
		val += makeRDF(this.getD(),second.getD(), weights, es, pos++);
		val += makeRDF(this.getE(),second.getE(), weights, es, pos++);
		val += makeRDF(this.getF(),second.getF(), weights, es, pos++);
		val += makeRDF(this.getG(),second.getG(), weights, es, pos++);
		val += makeRDF(this.getCost()-second.getCost(), weights, es, pos++);
		return val;
	}
	/**
	 *
	 * @param first
	 * @param second
	 * @param weights
	 * @param es
	 * @param pos
	 * @return
	 */
	private double makeRDF(boolean first, boolean second,
			double[] weights, double[] es, int pos)
	{return this.makeRDF(first^second ? 1.0 : 0.0, weights, es, pos);}
	/**
	 *
	 * @param makeTimeDistance
	 * @param weights
	 * @param es
	 * @param pos
	 * @return
	 */
	private double makeRDF(double value, double[] weights,
			double[] es, int pos)
	{
		double e = get(es,pos);
		double w = get(weights,pos);
		double de = value*e;
		return w/(1.0+(de*de));
	}
	/**
	 *
	 * @param minutesSinceZero2
	 * @param minutesSinceZero3
	 * @return
	 */
	private double makeTimeDistance(int firstTime,
			int secondTime)
	{
		int max;
		int min;
		if(firstTime < secondTime)
		{
			min = firstTime;
			max = secondTime;
		}
		else
		{
			min = secondTime;
			max = firstTime;
		}
		int firstDistance = max - min;
		int secondDistance = this.MINUTES_IN_A_DAY-max+min;
		return Math.min(firstDistance, secondDistance);
	}
	/**
	 *
	 * @param day2
	 * @param day3
	 * @param weights
	 * @param es
	 * @param i
	 * @return
	 */
	private double makeRDF(String s1, String s2, double[] weights,
			double[] es, int pos)
	{return this.makeRDF(s1.equals(s2) ? 0.0 : 1.0, weights, es, pos);}
	/**
	 *
	 * @param es
	 * @param pos
	 * @return
	 */
	private double get(double[] es, int pos)
	{
		if(pos < 0 || pos >= es.length)
		{return 0.0;}
		return es[pos];
	}
}