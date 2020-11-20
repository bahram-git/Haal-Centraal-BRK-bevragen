/*
 * Kadaster - BRK-Bevragen API
 * D.m.v. deze toepassing worden meerdere, korte bevragingen op de Basis Registratie Kadaster beschikbaar gesteld. Deze toepassing betreft het verstrekken van Kadastrale Onroerende Zaak informatie. 
 *
 * The version of the OpenAPI document: 1.2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.openapitools.client.model.KadasterNietNatuurlijkPersoonHal;

/**
 * KadasterNietNatuurlijkPersoonHalCollectieEmbedded
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-10-28T18:29:08.707Z[Etc/UTC]")
public class KadasterNietNatuurlijkPersoonHalCollectieEmbedded {
  public static final String SERIALIZED_NAME_KADASTER_NIET_NATUURLIJK_PERSONEN = "kadasterNietNatuurlijkPersonen";
  @SerializedName(SERIALIZED_NAME_KADASTER_NIET_NATUURLIJK_PERSONEN)
  private List<KadasterNietNatuurlijkPersoonHal> kadasterNietNatuurlijkPersonen = null;


  public KadasterNietNatuurlijkPersoonHalCollectieEmbedded kadasterNietNatuurlijkPersonen(List<KadasterNietNatuurlijkPersoonHal> kadasterNietNatuurlijkPersonen) {
    
    this.kadasterNietNatuurlijkPersonen = kadasterNietNatuurlijkPersonen;
    return this;
  }

  public KadasterNietNatuurlijkPersoonHalCollectieEmbedded addKadasterNietNatuurlijkPersonenItem(KadasterNietNatuurlijkPersoonHal kadasterNietNatuurlijkPersonenItem) {
    if (this.kadasterNietNatuurlijkPersonen == null) {
      this.kadasterNietNatuurlijkPersonen = new ArrayList<>();
    }
    this.kadasterNietNatuurlijkPersonen.add(kadasterNietNatuurlijkPersonenItem);
    return this;
  }

   /**
   * Get kadasterNietNatuurlijkPersonen
   * @return kadasterNietNatuurlijkPersonen
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<KadasterNietNatuurlijkPersoonHal> getKadasterNietNatuurlijkPersonen() {
    return kadasterNietNatuurlijkPersonen;
  }


  public void setKadasterNietNatuurlijkPersonen(List<KadasterNietNatuurlijkPersoonHal> kadasterNietNatuurlijkPersonen) {
    this.kadasterNietNatuurlijkPersonen = kadasterNietNatuurlijkPersonen;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    KadasterNietNatuurlijkPersoonHalCollectieEmbedded kadasterNietNatuurlijkPersoonHalCollectieEmbedded = (KadasterNietNatuurlijkPersoonHalCollectieEmbedded) o;
    return Objects.equals(this.kadasterNietNatuurlijkPersonen, kadasterNietNatuurlijkPersoonHalCollectieEmbedded.kadasterNietNatuurlijkPersonen);
  }

  @Override
  public int hashCode() {
    return Objects.hash(kadasterNietNatuurlijkPersonen);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class KadasterNietNatuurlijkPersoonHalCollectieEmbedded {\n");
    sb.append("    kadasterNietNatuurlijkPersonen: ").append(toIndentedString(kadasterNietNatuurlijkPersonen)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

