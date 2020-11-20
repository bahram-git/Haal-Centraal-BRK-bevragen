/* 
 * Kadaster - BRK-Bevragen API
 *
 * D.m.v. deze toepassing worden meerdere, korte bevragingen op de Basis Registratie Kadaster beschikbaar gesteld. Deze toepassing betreft het verstrekken van Kadastrale Onroerende Zaak informatie. 
 *
 * The version of the OpenAPI document: 1.2.0
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */


using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = Org.OpenAPITools.Client.OpenAPIDateConverter;

namespace Org.OpenAPITools.Model
{
    /// <summary>
    /// KadasterNietNatuurlijkPersoonHalCollectieEmbedded
    /// </summary>
    [DataContract]
    public partial class KadasterNietNatuurlijkPersoonHalCollectieEmbedded :  IEquatable<KadasterNietNatuurlijkPersoonHalCollectieEmbedded>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="KadasterNietNatuurlijkPersoonHalCollectieEmbedded" /> class.
        /// </summary>
        /// <param name="kadasterNietNatuurlijkPersonen">kadasterNietNatuurlijkPersonen.</param>
        public KadasterNietNatuurlijkPersoonHalCollectieEmbedded(List<KadasterNietNatuurlijkPersoonHal> kadasterNietNatuurlijkPersonen = default(List<KadasterNietNatuurlijkPersoonHal>))
        {
            this.KadasterNietNatuurlijkPersonen = kadasterNietNatuurlijkPersonen;
        }
        
        /// <summary>
        /// Gets or Sets KadasterNietNatuurlijkPersonen
        /// </summary>
        [DataMember(Name="kadasterNietNatuurlijkPersonen", EmitDefaultValue=false)]
        public List<KadasterNietNatuurlijkPersoonHal> KadasterNietNatuurlijkPersonen { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class KadasterNietNatuurlijkPersoonHalCollectieEmbedded {\n");
            sb.Append("  KadasterNietNatuurlijkPersonen: ").Append(KadasterNietNatuurlijkPersonen).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as KadasterNietNatuurlijkPersoonHalCollectieEmbedded);
        }

        /// <summary>
        /// Returns true if KadasterNietNatuurlijkPersoonHalCollectieEmbedded instances are equal
        /// </summary>
        /// <param name="input">Instance of KadasterNietNatuurlijkPersoonHalCollectieEmbedded to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(KadasterNietNatuurlijkPersoonHalCollectieEmbedded input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.KadasterNietNatuurlijkPersonen == input.KadasterNietNatuurlijkPersonen ||
                    this.KadasterNietNatuurlijkPersonen != null &&
                    input.KadasterNietNatuurlijkPersonen != null &&
                    this.KadasterNietNatuurlijkPersonen.SequenceEqual(input.KadasterNietNatuurlijkPersonen)
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.KadasterNietNatuurlijkPersonen != null)
                    hashCode = hashCode * 59 + this.KadasterNietNatuurlijkPersonen.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
