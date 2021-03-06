/**
 * 
 */
package kaggle.allstate.datastructures;
import java.util.ArrayList;
/**
 * 
 * @author Christoph Teichmann
 * created Mar 22, 2014 4:23:20 PM
 * @version 0.1
 */
public class SingleCostumer
{
	/**
	 * @param costumer_ID
	 */
	public SingleCostumer(String[] data)
	{
		this.costumer_ID = SingleObservation.makeSafeCopy(data, 0);
		this.addEntry(data);
	}
	/**
	 * @return the sale
	 */
	public SingleObservation getSale()
	{
		return sale;
	}

	/**
	 * @param sale the sale to set
	 */
	public void setSale(SingleObservation sale)
	{
		this.sale = sale;
	}

	/**
	 * @return the costumer_ID
	 */
	public String getCostumer_ID()
	{
		return costumer_ID;
	}
	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	@Override
	public String toString()
	{
		StringBuilder builder = new StringBuilder();
		builder.append("SingleCostumer [costumer_ID=");
		builder.append(costumer_ID);
		builder.append(", observations=");
		builder.append(observations);
		builder.append(", sale=");
		builder.append(sale);
		builder.append("]");
		return builder.toString();
	}
	/**
	 * 
	 */
	private final String costumer_ID;
	/**
	 * 
	 */
	private final ArrayList<SingleObservation> observations = new ArrayList<>();
	/**
	 * 
	 */
	private SingleObservation sale;
	/**
	 * 
	 *
	 * @param parts
	 */
	public void addEntry(String[] parts)
	{
		SingleObservation so = new SingleObservation(parts);
		if(so.isSale())
		{this.sale = so;}
		else
		{
			if(observations.size() < so.getShoppingPointnumber())
			{this.observations.add(null);}
			this.observations.set(so.getShoppingPointnumber(), so);
		}
	}
	/**
	 * 
	 *
	 * @param to
	 * @param fromEntry
	 * @param upToEntry
	 * @param weights
	 * @param es
	 * @return
	 */
	public double rdf(SingleCostumer to, int fromEntry, int upToEntry, double[][] weights, double[][] es)
	{
		double value = 0.0;
		for(int i=fromEntry;i<upToEntry;++i)
		{
			SingleObservation first = this.get(i);
			SingleObservation second = this.get(i);
			if(first == null || second == null)
			{continue;}
			double[] w = get(weights,i);
			double[] e = get(es,i);
			if(w != null && e != null)
			{value += first.makeRDF(second,w,e);}
		}
		return value;
	}
	/**
	 *
	 * @param es
	 * @param i
	 * @return
	 */
	private double[] get(double[][] ws, int l)
	{
		if(l < 0 || ws.length <= l)
		{return null;}
		return ws[l];
	}
	/**
	 *
	 * @param i
	 * @return
	 */
	private SingleObservation get(int i)
	{
		if(i >= this.size() || i < 0)
		{return null;}
		return this.observations.get(i);
	}

	/**
	 * 
	 *
	 * @return
	 */
	public int size()
	{return this.observations.size();}
}