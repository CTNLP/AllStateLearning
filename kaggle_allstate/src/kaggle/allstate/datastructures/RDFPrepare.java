/**
 * 
 */
package kaggle.allstate.datastructures;
import java.util.Arrays;
/**
 * @author Christoph Teichmann
 * created Mar 22, 2014 10:21:31 PM
 * @version 0.1
 */
public class RDFPrepare
{
	/**
	 * 
	 */
	private final double[] weights = new double[22];
	{Arrays.fill(weights, 1.0);}
	/**
	 * 
	 */
	private final double[] es = new double[22];
	{Arrays.fill(es, 1.0);}
	/**
	 * 
	 *
	 * @param w
	 */
	public void setDayWeight(double w)
	{this.weights[0] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setDayE(double e)
	{this.es[0] = e;}
	/**
	 * 
	 *
	 * @param w
	 */
	public void setTimeWeight(double w)
	{this.weights[1] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setTimeE(double e)
	{this.es[1] = e;}
	/**
	 * 
	 *
	 * @param w
	 */
	public void setStateWeight(double w)
	{this.weights[2] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setStateE(double e)
	{this.es[2] = e;}
	/**
	 * 
	 *
	 * @param w
	 */
	public void setLocationWeight(double w)
	{this.weights[3] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setLocationE(double e)
	{this.es[3] = e;}
	/**
	 * 
	 *
	 * @param w
	 */
	public void setGroupSizeWeight(double w)
	{this.weights[4] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setGroupSizeE(double e)
	{this.es[4] = e;}
	/**
	 * 
	 *
	 * @param w
	 */
	public void setHomeOwnerWeight(double w)
	{this.weights[5] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setHomeOwnerE(double e)
	{this.es[5] = e;}

	/**
	 * 
	 *
	 * @param w
	 */
	public void setCarAgeWeight(double w)
	{this.weights[6] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setCarAgeE(double e)
	{this.es[6] = e;}

	/**
	 * 
	 *
	 * @param w
	 */
	public void setCarValueWeight(double w)
	{this.weights[7] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setCarValueE(double e)
	{this.es[7] = e;}
	/**
	 * 
	 *
	 * @param w
	 */
	public void setRiskFactorWeight(double w)
	{this.weights[8] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setRiskFactorE(double e)
	{this.es[7] = e;}

	/**
	 * 
	 *
	 * @param w
	 */
	public void setAgeOldestWeight(double w)
	{this.weights[8] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setAgeOldestE(double e)
	{this.es[8] = e;}

	/**
	 * 
	 *
	 * @param w
	 */
	public void setAgeYoungest(double w)
	{this.weights[9] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setAgeYoungestE(double e)
	{this.es[9] = e;}

	/**
	 * 
	 *
	 * @param w
	 */
	public void setMarriedWeight(double w)
	{this.weights[10] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setMarriedE(double e)
	{this.es[10] = e;}

	/**
	 * 
	 *
	 * @param w
	 */
	public void setcPreviousWeight(double w)
	{this.weights[11] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setcPreviousE(double e)
	{this.es[11] = e;}

	/**
	 * 
	 *
	 * @param w
	 */
	public void setDurationPreviousWeight(double w)
	{this.weights[12] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setDurationPreviousE(double e)
	{this.es[12] = e;}
	/**
	 * 
	 *
	 * @param w
	 */
	public void setAWeight(double w)
	{this.weights[13] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setAE(double e)
	{this.es[13] = e;}
	/**
	 * 
	 *
	 * @param w
	 */
	public void setBWeight(double w)
	{this.weights[14] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setBE(double e)
	{this.es[14] = e;}
	/**
	 * 
	 *
	 * @param w
	 */
	public void setCWeight(double w)
	{this.weights[15] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setCE(double e)
	{this.es[15] = e;}
	/**
	 * 
	 *
	 * @param w
	 */
	public void setDWeight(double w)
	{this.weights[16] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setDE(double e)
	{this.es[16] = e;}
	/**
	 * 
	 *
	 * @param w
	 */
	public void setEWeight(double w)
	{this.weights[17] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setEE(double e)
	{this.es[17] = e;}
	/**
	 * 
	 *
	 * @param w
	 */
	public void setFWeight(double w)
	{this.weights[18] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setFE(double e)
	{this.es[18] = e;}
	/**
	 * 
	 *
	 * @param w
	 */
	public void setGWeight(double w)
	{this.weights[19] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setGE(double e)
	{this.es[19] = e;}
	/**
	 * 
	 *
	 * @param w
	 */
	public void setCostWeight(double w)
	{this.weights[20] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setCostE(double e)
	{this.es[20] = e;}
}