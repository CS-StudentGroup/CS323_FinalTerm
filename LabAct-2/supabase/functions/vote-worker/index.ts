import { serve } from "https://deno.land/std@0.168.0/http/server.ts"
import { createClient } from "https://esm.sh/@supabase/supabase-js@2"

serve(async (req) => {
  try {
    const { record } = await req.json();
    const { user_id, time_created } = record.payload;

    const receivedAt = Date.now() / 1000; // Convert ms to seconds to match Python
    const latency = receivedAt - time_created;

    console.log(`[LATENCY CHECK] User: ${user_id} | Delay: ${latency.toFixed(3)}s`);

    const supabase = createClient(
      Deno.env.get('SUPABASE_URL') ?? '',
      Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? ''
    )

    const { error: insertError } = await supabase
      .from('votes')
      .upsert({ 
        user_id, 
        poll_id, 
        choice,
        metadata: { processed_by: "vote-worker", original_node: node_id }
      }, { onConflict: 'user_id, poll_id' })

    if (insertError) throw insertError

    await supabase
      .from('vote_queue')
      .update({ status: 'processed' })
      .eq('id', record.id)

    return new Response(JSON.stringify({ status: "success" }), {
      headers: { "Content-Type": "application/json" },
      status: 200,
    })

  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      headers: { "Content-Type": "application/json" },
      status: 400,
    })
  }
})